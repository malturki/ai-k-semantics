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


class Child(Meter):
    pass


class DeleteOnly:
    @property
    def x(self):
        return 1

    @x.deleter
    def x(self):
        self.deleted = True


class ReadOnly:
    @property
    def x(self):
        return 2


p = Plain()
p.kind = 7
result = result and p.kind == 7
del p.kind
result = result and p.kind == 1
p.extra = 9
del p.extra
try:
    p.extra
    result = False
except AttributeError:
    result = result and True

m = Meter(3)
result = result and m.value == 3
del m.value
result = result and m.value == -1

c = Child(4)
del c.value
result = result and c.value == -1

d = DeleteOnly()
try:
    d.x = 5
    result = False
except AttributeError:
    result = result and d.x == 1
del d.x
result = result and d.deleted

ro = ReadOnly()
try:
    del ro.x
    result = False
except AttributeError:
    result = result and ro.x == 2

assert result
result
