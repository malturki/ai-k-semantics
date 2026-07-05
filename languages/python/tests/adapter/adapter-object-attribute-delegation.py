result = True


class Delegating:
    def __setattr__(self, name, value):
        if name == "x":
            object.__setattr__(self, name, value + 1)
            return
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name == "keep":
            return
        object.__delattr__(self, name)


d = Delegating()
d.x = 4
result = result and d.x == 5
result = result and setattr(d, "y", 6) is None
result = result and d.y == 6
result = result and object.__setattr__(d, "raw", 9) is None
result = result and d.raw == 9

d.keep = 10
d.drop = 11
del d.keep
result = result and d.keep == 10
del d.drop
try:
    d.drop
    result = False
except AttributeError:
    result = result and True

result = result and object.__delattr__(d, "keep") is None
try:
    d.keep
    result = False
except AttributeError:
    result = result and True

try:
    object.__setattr__(d, 1, 2)
    result = False
except TypeError:
    result = result and True

try:
    object.__delattr__(d, 1)
    result = False
except TypeError:
    result = result and True


class Meter:
    def __init__(self, value):
        self.value = value

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        object.__delattr__(self, name)

    @property
    def value(self):
        return self.raw

    @value.setter
    def value(self, new):
        self.raw = new

    @value.deleter
    def value(self):
        self.raw = -1


m = Meter(3)
result = result and m.value == 3
m.value = 4
result = result and m.value == 4
result = result and delattr(m, "value") is None
result = result and m.value == -1

result
