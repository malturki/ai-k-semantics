result = True


class Base:
    def __getattribute__(self, name):
        if name == "virtual":
            return 10
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        if name == "fallback":
            return 20
        if name == "prop":
            return 30
        raise AttributeError

    def __setattr__(self, name, value):
        if name == "bump":
            object.__setattr__(self, name, value + 1)
            return
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name == "keep":
            return
        object.__delattr__(self, name)

    @property
    def prop(self):
        raise AttributeError

    @property
    def boom(self):
        raise ValueError


class Child(Base):
    pass


class Override(Base):
    def __getattr__(self, name):
        if name == "fallback":
            return 99
        raise AttributeError


c = Child()
c.bump = 4
c.normal = 6
c.keep = 8

result = result and c.virtual == 10
result = result and c.bump == 5
result = result and c.normal == 6
result = result and c.fallback == 20
result = result and c.prop == 30
result = result and getattr(c, "virtual") == 10
result = result and getattr(c, "fallback") == 20
result = result and getattr(c, "absent", 7) == 7
result = result and hasattr(c, "virtual")
result = result and hasattr(c, "fallback")
result = result and not hasattr(c, "absent")

del c.keep
result = result and c.keep == 8
del c.normal
result = result and not hasattr(c, "normal")

try:
    object.__getattribute__(c, "prop")
    result = False
except AttributeError:
    result = result and True

try:
    c.boom
    result = False
except ValueError:
    result = result and True

o = Override()
result = result and o.fallback == 99

result
