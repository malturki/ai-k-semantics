result = True


class Counter:
    base = 10
    kind = 1

    def __init__(self, start):
        self.value = start
        self.kind = 2

    def total(self):
        return self.value + self.base

    def bump(self, amount):
        self.value = self.value + amount
        return self.value


c = Counter(5)
alias = c

result = result and c.value == 5
result = result and c.base == 10
result = result and c.kind == 2
result = result and Counter.kind == 1
result = result and c.total() == 15
result = result and Counter.total(c) == 15
result = result and c.bump(7) == 12
result = result and alias.value == 12
result = result and c.total() == 22
result = result and callable(c.total)
result = result and callable(getattr(c, "total"))
result = result and getattr(c, "value") == 12
result = result and getattr(c, "base") == 10
result = result and getattr(c, "missing", 99) == 99
result = result and hasattr(c, "value")
result = result and hasattr(c, "total")
result = result and not hasattr(c, "missing")

missing_error = False
try:
    getattr(c, "missing")
except AttributeError:
    missing_error = True

result = result and missing_error

assert result
result
