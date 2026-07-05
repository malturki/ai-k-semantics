result = True


class Hooked:
    present = 2

    def __getattribute__(self, name):
        if name == "virtual":
            return 40
        if name == "boom":
            raise ValueError
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        if name == "fallback":
            return 50
        raise AttributeError


h = Hooked()
h.instance = 10

result = result and h.virtual == 40
result = result and h.instance == 10
result = result and h.present == 2
result = result and h.fallback == 50
result = result and getattr(h, "virtual") == 40
result = result and getattr(h, "fallback") == 50
result = result and getattr(h, "absent", 99) == 99
result = result and hasattr(h, "virtual")
result = result and hasattr(h, "fallback")
result = result and not hasattr(h, "absent")

try:
    h.boom
    result = False
except ValueError:
    result = result and True

try:
    getattr(h, "boom")
    result = False
except ValueError:
    result = result and True

try:
    hasattr(h, "boom")
    result = False
except ValueError:
    result = result and True

try:
    getattr(h, "missing", 1 // 0)
    result = False
except ZeroDivisionError:
    result = result and True

result
