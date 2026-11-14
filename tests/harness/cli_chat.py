"""Temporary local provider: runs each call through a local agent CLI (subscription access).

Interim solution for development only. To remove it: delete this file, the "cli" line in
llm.py, the "cli" block in tests/config.json and the "Local CLI" section in the skill.

Isolation per call: fresh empty temp directory as working directory, tools off via CLI
switches, no session persistence, reply used as plain text only. The caller holds the
conversation; earlier turns are rendered into one prompt, so every call is stateless.
Local results are a different access than API runs and do not replace the CI gate.
"""
import json
import os
import shutil
import subprocess
import tempfile
import time

from .llm import Reply

# Placeholders in a command: {model} {system_file} {schema_file} {output_file} {workdir} {effort}.
# The prompt is passed on stdin. An argument containing a placeholder whose value is empty is
# dropped together with the switch right before it (e.g. "--model", "{model}").
PROFILES = {
    "claude": {
        "command": ["claude", "-p", "--output-format", "json",
                    "--tools", "", "--strict-mcp-config", "--setting-sources", "",
                    "--disable-slash-commands", "--no-session-persistence",
                    "--model", "{model}", "--effort", "{effort}",
                    "--system-prompt-file", "{system_file}", "--json-schema", "{schema_json}"],
        "parse": "claude_json",
        "system": "flag",
    },
    "codex": {
        "command": ["codex", "exec", "--ephemeral", "--skip-git-repo-check", "--ignore-user-config", "--ignore-rules",
                    "--sandbox", "read-only", "--color", "never",
                    "-C", "{workdir}", "-m", "{model}",
                    "-c", "model_reasoning_effort={effort}",
                    "--output-schema", "{schema_file}", "--output-last-message", "{output_file}", "-"],
        "parse": "output_file",
        "system": "prepend",
    },
}


def _text(content):
    if isinstance(content, str):
        return content
    return "".join(b.get("text", "") for b in content if b.get("type") == "text")


def render(messages):
    """One stateless prompt from the caller's message list."""
    if len(messages) == 1:
        return _text(messages[0]["content"])
    parts = ["The conversation so far is below. Reply only with your next message as the assistant, "
             "without any label.\n"]
    for m in messages:
        parts.append(f"[{m['role']}]\n{_text(m['content'])}\n")
    return "\n".join(parts)


def _fill(command, values):
    out = []
    for arg in command:
        keys = [k for k in values if "{" + k + "}" in arg]
        if any(not values[k] for k in keys):
            if out and out[-1].startswith("-"):
                out.pop()  # drop the switch that belonged to the empty value
            continue
        for k in keys:
            arg = arg.replace("{" + k + "}", values[k])
        out.append(arg)
    return out


class CliChat:
    def __init__(self):
        from .common import load_config
        cfg = load_config().get("cli") or {}
        name = os.environ.get("TEST_CLI_PROFILE") or cfg.get("profile") or "claude"
        profile = dict(PROFILES.get(name, {}))
        profile.update((cfg.get("profiles") or {}).get(name, {}))
        if not profile.get("command"):
            raise SystemExit(f"CLI-Profil '{name}' unbekannt: in tests/config.json unter cli.profiles anlegen.")
        if not shutil.which(profile["command"][0]):
            raise SystemExit(f"CLI '{profile['command'][0]}' nicht gefunden. Kein stiller Wechsel zur API.")
        self.name = name
        self.profile = profile
        self.timeout = cfg.get("timeout_s", 600)
        self.use_model = cfg.get("pass_model", True)

    def send(self, model, messages, system=None, max_tokens=4000, effort=None, json_schema=None):
        prompt = render(messages)
        if system and self.profile.get("system") != "flag":
            prompt = f"{system}\n\n---\n\n{prompt}"
            system = None
        with tempfile.TemporaryDirectory(prefix="prompt-test-") as tmp:
            work = os.path.join(tmp, "work")
            os.mkdir(work)  # empty working directory; helper files stay outside it
            files = {"system_file": system, "schema_file": json.dumps(json_schema) if json_schema else None}
            values = {"workdir": work, "output_file": os.path.join(tmp, "reply.txt"),
                      "model": model if self.use_model else "", "effort": effort or "",
                      "schema_json": files["schema_file"] or ""}
            for key, data in files.items():
                values[key] = ""
                if data:
                    values[key] = os.path.join(tmp, key + ".txt")
                    with open(values[key], "w", encoding="utf-8") as f:
                        f.write(data)
            cmd = _fill(self.profile["command"], values)
            started = time.monotonic()
            p = subprocess.run(cmd, input=prompt, cwd=work, capture_output=True, text=True,
                               encoding="utf-8", timeout=self.timeout)
            seconds = round(time.monotonic() - started, 1)
            if p.returncode != 0:
                raise RuntimeError(f"CLI '{self.name}' Fehler {p.returncode}: {(p.stderr or p.stdout)[-800:]}")
            text, usage, reported, stop = self._parse(p.stdout, values["output_file"])
        usage["seconds"] = seconds
        return Reply(text=text, content=[{"type": "text", "text": text}], usage=usage,
                     stop_reason=stop, model=reported or f"{self.name}:{model}")

    def _parse(self, stdout, output_file):
        how = self.profile.get("parse", "text")
        if how == "claude_json":
            d = json.loads(stdout)
            if d.get("is_error"):
                raise RuntimeError(f"CLI '{self.name}': {d.get('result', '')[:800]}")
            text = d.get("result", "")
            if d.get("structured_output") is not None:
                text = json.dumps(d["structured_output"], ensure_ascii=False)
            u = d.get("usage") or {}
            usage = {"input": u.get("input_tokens", 0), "output": u.get("output_tokens", 0),
                     "cache_write": u.get("cache_creation_input_tokens", 0),
                     "cache_read": u.get("cache_read_input_tokens", 0)}
            models = list((d.get("modelUsage") or {}).keys())
            return text, usage, ",".join(models), d.get("stop_reason") or d.get("subtype", "")
        if how == "output_file" and os.path.exists(output_file):
            with open(output_file, encoding="utf-8") as f:
                return f.read().strip(), {}, "", ""
        return stdout.strip(), {}, "", ""
