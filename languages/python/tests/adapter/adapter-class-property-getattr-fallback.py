result = True


class WithFallback:
    def __init__(self):
        self.raw = 5

    @property
    def ok(self):
        return self.raw

    @property
    def missing_prop(self):
        raise AttributeError

    @property
    def boom(self):
        raise ValueError

    def __getattr__(self, name):
        if name == "missing_prop":
            return 77
        raise AttributeError


w = WithFallback()

result = result and w.ok == 5
result = result and w.missing_prop == 77
result = result and getattr(w, "missing_prop") == 77
result = result and getattr(w, "missing_prop", 99) == 77
result = result and hasattr(w, "missing_prop")

try:
    w.boom
    result = False
except ValueError:
    result = result and True

try:
    getattr(w, "boom")
    result = False
except ValueError:
    result = result and True

try:
    hasattr(w, "boom")
    result = False
except ValueError:
    result = result and True


class WithoutFallback:
    @property
    def missing_prop(self):
        raise AttributeError


n = WithoutFallback()

try:
    n.missing_prop
    result = False
except AttributeError:
    result = result and True

result = result and getattr(n, "missing_prop", 99) == 99
result = result and not hasattr(n, "missing_prop")

result
