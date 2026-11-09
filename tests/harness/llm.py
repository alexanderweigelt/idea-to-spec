"""Narrow, replaceable model connection.

Every provider implements one method:
    send(model, messages, system=None, max_tokens=..., effort=None, json_schema=None) -> Reply
`messages` is a plain list of {"role": "user"|"assistant", "content": str | list}.
Each call is stateless: the caller holds the conversation. No sandbox, no tools,
no file access – the tested model only sees what is in `messages`.
To add a provider, write a class with `send` and register it in `connect`.
"""
from dataclasses import dataclass, field


@dataclass
class Reply:
    text: str
    content: list              # content to append unchanged as the assistant turn
    usage: dict = field(default_factory=dict)  # input, output, cache_write, cache_read
    stop_reason: str = ""
    model: str = ""            # model id as reported by the provider


class AnthropicChat:
    def __init__(self):
        import anthropic  # pip install -r tests/requirements.txt
        self.client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY or `ant auth login`

    def send(self, model, messages, system=None, max_tokens=4000, effort=None, json_schema=None):
        kwargs = dict(
            model=model,
            max_tokens=max_tokens,
            messages=messages,
            # Moving cache point: the whole previous conversation is billed at the cache-read price.
            cache_control={"type": "ephemeral"},
        )
        if system:
            kwargs["system"] = system
        output_config = {}
        if effort:
            output_config["effort"] = effort
        if json_schema:
            output_config["format"] = {"type": "json_schema", "schema": json_schema}
        if output_config:
            kwargs["output_config"] = output_config
        # No server-side fallback on purpose: a test must not silently switch the model.
        with self.client.messages.stream(**kwargs) as stream:
            msg = stream.get_final_message()
        u = msg.usage
        return Reply(
            text="".join(b.text for b in msg.content if b.type == "text"),
            content=[b.model_dump(exclude_none=True) for b in msg.content],
            usage={
                "input": u.input_tokens or 0,
                "output": u.output_tokens or 0,
                "cache_write": getattr(u, "cache_creation_input_tokens", 0) or 0,
                "cache_read": getattr(u, "cache_read_input_tokens", 0) or 0,
            },
            stop_reason=msg.stop_reason or "",
            model=msg.model,
        )


PROVIDERS = {"anthropic": AnthropicChat}


def connect(name):
    return PROVIDERS[name]()
