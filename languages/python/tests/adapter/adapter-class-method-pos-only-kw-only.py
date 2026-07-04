class Worker:
    base = 4

    def __init__(self, start=base, /, step=1, *, extra, scale=2):
        self.total = (start + step + extra) * scale

    def combine(self, value, /, bump, *, scale):
        return self.total + (value + bump) * scale

    def defaulted(self, value=base, /, bump=1, *, scale, offset=2):
        return self.total + value * scale + bump + offset

    def required(self, value, /, *, scale):
        return self.total + value * scale

    base = 40


class Child(Worker):
    pass


w = Worker(5, 2, extra=3, scale=2)
defaulted = Worker(extra=2)
child = Child(3, 1, extra=1)

plain_ok = (
    w.total == 20
    and defaulted.total == 14
    and child.total == 10
    and w.combine(2, 3, scale=4) == 40
    and Worker.combine(w, 2, 3, scale=2) == 30
    and getattr(w, "combine")(1, 2, scale=5) == 35
    and child.combine(1, 2, scale=3) == 19
    and w.defaulted(scale=2) == 31
    and w.defaulted(3, 4, scale=2, offset=5) == 35
    and w.required(3, scale=5) == 35
)


class Tools:
    seed = 5
    kind = 10

    @staticmethod
    def mix(value, /, factor, *, scale):
        return value * factor * scale

    @staticmethod
    def defaulted(value=seed, /, factor=2, *, scale, offset=1):
        return value * factor * scale + offset

    @staticmethod
    def only(value, /, *, scale):
        return value * scale

    @classmethod
    def tag(cls, value, /, factor, *, scale):
        return cls.kind + value * factor * scale

    @classmethod
    def defaulted_tag(cls, value=seed, /, factor=2, *, scale, offset=1):
        return cls.kind + value * factor * scale + offset

    @classmethod
    def req(cls, value, /, *, scale):
        return cls.kind + value * scale

    seed = 50


class MoreTools(Tools):
    kind = 100


staticmethod_ok = (
    Tools.mix(2, 3, scale=4) == 24
    and Tools.defaulted(scale=3) == 31
    and Tools.defaulted(3, 4, scale=2, offset=5) == 29
    and Tools.only(5, scale=4) == 20
)

classmethod_ok = (
    Tools.tag(2, 3, scale=4) == 34
    and MoreTools.tag(2, 3, scale=4) == 124
    and Tools.defaulted_tag(scale=2) == 31
    and MoreTools.defaulted_tag(3, 4, scale=2, offset=5) == 129
    and MoreTools.req(2, scale=5) == 110
    and getattr(MoreTools(), "req")(3, scale=4) == 112
)


def identity(cls):
    return cls


@identity
class Decorated:
    seed = 2

    def calc(self, value=seed, /, *, scale):
        return value * scale


@identity
class DecoratedChild(Decorated):
    def add(self, value, /, *, scale):
        return self.calc(value, scale=scale) + 1


decorated_ok = Decorated().calc(scale=3) == 6 and DecoratedChild().add(4, scale=5) == 21

keyword_plain = False
try:
    w.combine(value=2, bump=3, scale=4)
except TypeError:
    keyword_plain = True

missing_plain_kw = False
try:
    w.combine(2, 3)
except TypeError:
    missing_plain_kw = True

duplicate_plain = False
try:
    w.combine(2, 3, bump=4, scale=5)
except TypeError:
    duplicate_plain = True

keyword_static = False
try:
    Tools.mix(value=1, factor=2, scale=3)
except TypeError:
    keyword_static = True

missing_static_kw = False
try:
    Tools.only(2)
except TypeError:
    missing_static_kw = True

keyword_class = False
try:
    Tools.tag(value=1, factor=2, scale=3)
except TypeError:
    keyword_class = True

missing_class_kw = False
try:
    Tools.req(2)
except TypeError:
    missing_class_kw = True

errors_ok = (
    keyword_plain
    and missing_plain_kw
    and duplicate_plain
    and keyword_static
    and missing_static_kw
    and keyword_class
    and missing_class_kw
)

result = plain_ok and staticmethod_ok and classmethod_ok and decorated_ok and errors_ok
assert result
result
