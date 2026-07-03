result = True


class Box:
    kind = 4

    def __init__(self, value):
        self.value = value

    @property
    def doubled(self):
        return self.value * 2

    @property
    def tagged(self):
        return self.kind + self.value


class Child(Box):
    kind = 10


class Counter:
    def __init__(self):
        self.n = 0

    @property
    def next_value(self):
        self.n = self.n + 1
        return self.n


b = Box(3)
c = Child(5)
counter = Counter()

result = result and b.doubled == 6
result = result and getattr(b, "doubled") == 6
result = result and getattr(b, "missing", 99) == 99
result = result and c.doubled == 10
result = result and c.tagged == 15
result = result and getattr(c, "tagged") == 15
result = result and counter.next_value == 1
result = result and counter.next_value == 2
result = result and counter.n == 2
result = result and not callable(Box.doubled)
result = result and not callable(getattr(Box, "doubled"))
result = result and not callable(Child.tagged)
result = result and bool(Box.doubled)

assert result
result
