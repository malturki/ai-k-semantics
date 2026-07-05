result = True


class Plain:
    kind = 1


class Meter:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.raw

    @value.setter
    def value(self, new):
        self.raw = new


class ReadOnly:
    @property
    def x(self):
        return 2


p = Plain()
result = result and p.kind == 1
result = result and setattr(p, "kind", 7) is None
result = result and p.kind == 7
del p.kind
result = result and p.kind == 1

name = "extra"
result = result and setattr(p, name, 9) is None
result = result and p.extra == 9
result = result and getattr(p, "extra") == 9
result = result and setattr(p, name, 10) is None
result = result and p.extra == 10

result = result and setattr(p, "not an id", 11) is None
result = result and getattr(p, "not an id") == 11
result = result and hasattr(p, "not an id")

m = Meter(3)
result = result and m.value == 3
result = result and setattr(m, "value", 5) is None
result = result and m.value == 5

ro = ReadOnly()
try:
    setattr(ro, "x", 8)
    result = False
except AttributeError:
    result = result and ro.x == 2

try:
    setattr(p, 1, 99)
    result = False
except TypeError:
    result = result and True

try:
    setattr(p, 1, 1 / 0)
    result = False
except ZeroDivisionError:
    result = result and True

result
