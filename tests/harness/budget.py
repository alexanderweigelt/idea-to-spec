"""Hard cost limit. Checked BEFORE every call with the worst case, booked AFTER with real usage."""


class BudgetExceeded(Exception):
    pass


class Budget:
    def __init__(self, prices, per_run, per_test):
        self.prices = prices
        self.per_run = per_run
        self.per_test = per_test
        self.total = 0.0
        self.run = 0.0
        self.by_role = {}
        self.run_roles = {}

    def start_run(self):
        self.run = 0.0
        self.run_roles = {}

    def price(self, model):
        if model not in self.prices:
            raise KeyError(f"Kein Preis für {model} in tests/config.json – ohne Preis kein Lauf.")
        return self.prices[model]

    def cost(self, model, usage):
        p = self.price(model)
        return (usage.get("input", 0) * p["input"]
                + usage.get("cache_write", 0) * p["input"] * 1.25
                + usage.get("cache_read", 0) * p["cache_read"]
                + usage.get("output", 0) * p["output"]) / 1e6

    def guard(self, model, input_chars, max_tokens):
        """Worst case: whole input uncached (chars/3 is a generous token estimate) plus max_tokens output."""
        worst = self.cost(model, {"input": input_chars / 3 * 1.25, "output": max_tokens})
        if self.run + worst > self.per_run:
            raise BudgetExceeded(f"Lauf-Grenze {self.per_run} USD: bisher {self.run:.3f}, nächster Aufruf bis {worst:.3f}")
        if self.total + worst > self.per_test:
            raise BudgetExceeded(f"Testlauf-Grenze {self.per_test} USD: bisher {self.total:.3f}, nächster Aufruf bis {worst:.3f}")

    def book(self, role, model, usage):
        c = self.cost(model, usage)
        self.run += c
        self.total += c
        for table in (self.by_role, self.run_roles):
            r = table.setdefault(role, {"model": model, "calls": 0, "input": 0, "output": 0,
                                        "cache_write": 0, "cache_read": 0, "usd": 0.0})
            r["calls"] += 1
            for k in ("input", "output", "cache_write", "cache_read"):
                r[k] += usage.get(k, 0)
            r["usd"] += c
        return c
