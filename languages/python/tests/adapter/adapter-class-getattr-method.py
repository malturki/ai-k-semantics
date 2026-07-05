result = True


class Fallback:
    present = 2

    def __getattr__(self, name):
        if name == "missing":
            return 30
        if name == "dynamic":
            return self.present + 4
        if name == "boom":
            raise ValueError
        raise AttributeError


f = Fallback()
f.instance = 10

result = result and f.instance == 10
result = result and f.present == 2
result = result and f.missing == 30
result = result and getattr(f, "dynamic") == 6
result = result and getattr(f, "missing", 99) == 30
result = result and getattr(f, "absent", 99) == 99
result = result and getattr(f, "instance", 99) == 10
result = result and getattr(f, "present", 99) == 2
result = result and hasattr(f, "missing")
result = result and not hasattr(f, "absent")

try:
    getattr(f, "boom")
    result = False
except ValueError:
    result = result and True

try:
    getattr(f, "boom", 99)
    result = False
except ValueError:
    result = result and True

try:
    hasattr(f, "boom")
    result = False
except ValueError:
    result = result and True

try:
    getattr(f, "missing", 1 // 0)
    result = False
except ZeroDivisionError:
    result = result and True

result
