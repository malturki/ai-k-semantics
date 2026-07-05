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

    @value.deleter
    def value(self):
        self.raw = -1


class ReadOnly:
    @property
    def x(self):
        return 2


p = Plain()
p.kind = 7
result = result and p.kind == 7
result = result and delattr(p, "kind") is None
result = result and p.kind == 1

p.extra = 9
name = "extra"
result = result and delattr(p, name) is None
try:
    p.extra
    result = False
except AttributeError:
    result = result and True

m = Meter(3)
result = result and m.value == 3
result = result and delattr(m, "value") is None
result = result and m.value == -1

ro = ReadOnly()
try:
    delattr(ro, "x")
    result = False
except AttributeError:
    result = result and ro.x == 2

try:
    delattr(p, "missing")
    result = False
except AttributeError:
    result = result and True

try:
    delattr(p, 1)
    result = False
except TypeError:
    result = result and True

result
