result = True


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

    @value.getter
    def value(self):
        return self.raw * 2


class Child(Meter):
    pass


class GetterOnly:
    @property
    def x(self):
        return 1

    @x.getter
    def x(self):
        return 2


class SetterThenGetter:
    def __init__(self):
        self.raw = 0

    @property
    def x(self):
        return self.raw

    @x.setter
    def x(self, new):
        self.raw = new

    @x.getter
    def x(self):
        return self.raw + 10


class DeleterThenGetter:
    @property
    def x(self):
        return 1

    @x.deleter
    def x(self):
        self.deleted = True

    @x.getter
    def x(self):
        return 2


m = Meter(3)
result = result and m.value == 6
m.value = 5
result = result and m.value == 10
del m.value
result = result and m.value == -2

c = Child(4)
result = result and c.value == 8
c.value = 6
result = result and c.value == 12
del c.value
result = result and c.value == -2

g = GetterOnly()
result = result and g.x == 2
try:
    g.x = 3
    result = False
except AttributeError:
    result = result and g.x == 2
try:
    del g.x
    result = False
except AttributeError:
    result = result and g.x == 2

s = SetterThenGetter()
s.x = 5
result = result and s.x == 15
try:
    del s.x
    result = False
except AttributeError:
    result = result and s.x == 15

d = DeleterThenGetter()
result = result and d.x == 2
try:
    d.x = 7
    result = False
except AttributeError:
    result = result and d.x == 2
del d.x
result = result and d.deleted and d.x == 2

assert result
result
