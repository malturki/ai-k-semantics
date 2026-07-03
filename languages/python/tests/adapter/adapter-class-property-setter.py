result = True


class Meter:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.raw

    @value.setter
    def value(self, new):
        self.raw = new * 2


class Child(Meter):
    pass


class ReadOnly:
    @property
    def x(self):
        return 1


m = Meter(3)
c = Child(4)

result = result and m.value == 6
result = result and m.raw == 6
m.value = 5
result = result and m.value == 10
result = result and m.raw == 10
result = result and getattr(m, "value") == 10
c.value = 6
result = result and c.value == 12
result = result and c.raw == 12
result = result and not callable(Meter.value)
result = result and bool(Meter.value)

ro = ReadOnly()
try:
    ro.x = 2
    result = False
except AttributeError:
    result = result and ro.x == 1

assert result
result
