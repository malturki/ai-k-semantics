result = True


class Watch:
    def __delattr__(self, name):
        if name == "x":
            raise ValueError
        if name == "y":
            raise ZeroDivisionError


w = Watch()
w.x = 1
w.y = 2
w.z = 3

try:
    delattr(w, "x")
    result = False
except ValueError:
    result = result and hasattr(w, "x")

try:
    del w.y
    result = False
except ZeroDivisionError:
    result = result and hasattr(w, "y")

result = result and delattr(w, "z") is None
result = result and hasattr(w, "z")

result = result and delattr(w, "missing") is None
result = result and not hasattr(w, "missing")

result
