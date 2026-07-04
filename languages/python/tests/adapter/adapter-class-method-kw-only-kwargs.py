result = True


def identity(cls):
    return cls


class Collector:
    seed = 4

    def __init__(self, start=seed, *, scale, offset=1, **kw):
        self.total = (start + kw["bonus"]) * scale + offset

    def pack(self, label, *, scale, **kw):
        return (label, self.total * scale, kw["tag"], len(kw))

    def defaulted(self, value=seed, *, scale=2, offset=1, **kw):
        return value * scale + offset + kw["bonus"] + len(kw)

    def only(self, *, scale, **kw):
        return self.total * scale + kw["bonus"]

    seed = 40


class Child(Collector):
    pass


c = Collector(scale=3, bonus=2)
explicit = Collector(5, scale=2, offset=3, bonus=4, extra=8)
child = Child(5, scale=2, bonus=3)

plain_ok = (
    c.total == 19
    and explicit.total == 21
    and child.total == 17
    and c.pack("x", scale=2, tag="ok", spare=9) == ("x", 38, "ok", 2)
    and Collector.pack(c, "y", scale=1, tag="direct") == ("y", 19, "direct", 1)
    and c.defaulted(bonus=5) == 15
    and c.only(scale=2, bonus=1) == 39
    and child.pack("z", scale=1, tag="child") == ("z", 17, "child", 1)
    and getattr(child, "only")(scale=1, bonus=4) == 21
)


class Tools:
    seed = 5
    kind = 10

    @staticmethod
    def mix(head, *, scale, **kw):
        return head * scale + kw["bonus"] + len(kw)

    @staticmethod
    def defaulted(head=seed, *, scale=2, offset=1, **kw):
        return head * scale + offset + kw["bonus"] + len(kw)

    @staticmethod
    def only(*, scale, **kw):
        return scale + kw["bonus"] + len(kw)

    @classmethod
    def tag(cls, head, *, scale, **kw):
        return cls.kind + head * scale + kw["bonus"] + len(kw)

    @classmethod
    def defaulted_tag(cls, head=seed, *, scale=2, offset=1, **kw):
        return cls.kind + head * scale + offset + kw["bonus"] + len(kw)

    seed = 50


class MoreTools(Tools):
    kind = 100


staticmethod_ok = (
    Tools.mix(3, scale=4, bonus=1) == 14
    and Tools.defaulted(bonus=6) == 18
    and Tools.only(scale=4, bonus=5) == 10
    and Tools().only(scale=2, bonus=3, extra=4) == 7
)

classmethod_ok = (
    Tools.tag(3, scale=2, bonus=1) == 18
    and MoreTools.defaulted_tag(bonus=6) == 118
    and getattr(MoreTools(), "tag")(2, scale=3, bonus=4, marker=9) == 112
)


@identity
class Decorated:
    seed = 3

    def calc(self, value=seed, *, scale=2, **kw):
        return value * scale + kw["bonus"] + len(kw)


@identity
class DecoratedChild(Decorated):
    def add(self, value, *, scale, offset=1, **kw):
        return value * scale + offset + kw["bonus"] + len(kw)


decorated_ok = (
    Decorated().calc(bonus=4) == 11
    and Decorated().calc(2, scale=3, bonus=4, extra=5) == 12
    and DecoratedChild().add(4, scale=3, bonus=2) == 16
)

missing_plain_kw = False
try:
    c.pack("x", tag="bad")
except TypeError:
    missing_plain_kw = True

duplicate_plain = False
try:
    c.pack("x", label="dup", scale=1, tag="ok")
except TypeError:
    duplicate_plain = True

missing_static_kw = False
try:
    Tools.mix(2, bonus=1)
except TypeError:
    missing_static_kw = True

duplicate_static = False
try:
    Tools.mix(2, head=3, scale=1, bonus=1)
except TypeError:
    duplicate_static = True

missing_class_kw = False
try:
    Tools.tag(2, bonus=1)
except TypeError:
    missing_class_kw = True

errors_ok = (
    missing_plain_kw
    and duplicate_plain
    and missing_static_kw
    and duplicate_static
    and missing_class_kw
)

result = plain_ok and staticmethod_ok and classmethod_ok and decorated_ok and errors_ok
assert result
result
