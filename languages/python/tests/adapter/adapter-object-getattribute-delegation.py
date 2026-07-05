result = True


class Plain:
    kind = 1

    def method(self):
        return self.kind


p = Plain()
p.extra = 2

method = object.__getattribute__(p, "method")
result = result and object.__getattribute__(p, "extra") == 2
result = result and object.__getattribute__(p, "kind") == 1
result = result and method() == 1


class Meter:
    @property
    def value(self):
        return self.raw


m = Meter()
m.raw = 3
result = result and object.__getattribute__(m, "value") == 3


class Dynamic:
    def __getattr__(self, name):
        if name == "missing":
            return 9
        raise AttributeError


d = Dynamic()
result = result and d.missing == 9

try:
    object.__getattribute__(d, "missing")
    result = False
except AttributeError:
    result = result and True

try:
    object.__getattribute__(d, 1)
    result = False
except TypeError:
    result = result and True

result
