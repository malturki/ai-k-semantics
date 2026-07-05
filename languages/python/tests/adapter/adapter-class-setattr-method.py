result = True


class Watch:
    def __setattr__(self, name, value):
        if name == "x" and value == 3:
            raise ValueError
        if name == "y" and value == 4:
            raise ZeroDivisionError


w = Watch()

try:
    setattr(w, "x", 3)
    result = False
except ValueError:
    result = result and not hasattr(w, "x")

try:
    w.y = 4
    result = False
except ZeroDivisionError:
    result = result and not hasattr(w, "y")

result = result and setattr(w, "z", 5) is None
result = result and not hasattr(w, "z")

result
