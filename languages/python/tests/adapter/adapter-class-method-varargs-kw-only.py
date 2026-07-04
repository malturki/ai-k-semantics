result = True


class Collector:
    seed = 4

    def __init__(self, start=seed, *items, extra, scale=2):
        self.total = (start + len(items) + extra) * scale

    def pack(self, label, *items, scale):
        return (self.total, label, len(items), items[0], items[1], scale)

    def defaulted(self, value=seed, *items, scale=2, offset=1):
        return self.total + value * scale + len(items) + offset

    def only(self, *items, scale):
        return (self.total, len(items), scale)

    seed = 40


class Child(Collector):
    pass


c = Collector(1, 2, 3, extra=4, scale=2)
defaulted = Collector(extra=1)
child = Child(2, 9, extra=1)

plain_ok = (
    c.total == 14
    and defaulted.total == 10
    and child.total == 8
    and c.pack("p", 5, 6, scale=3) == (14, "p", 2, 5, 6, 3)
    and Collector.pack(c, "q", 7, 8, scale=4) == (14, "q", 2, 7, 8, 4)
    and getattr(c, "only")(1, 2, 3, scale=5) == (14, 3, 5)
    and defaulted.defaulted(offset=3) == 21
    and c.defaulted(2, 9, 10, scale=3, offset=4) == 26
    and child.defaulted(offset=1) == 17
)


class Tools:
    seed = 5
    kind = 10

    @staticmethod
    def mix(head, *tail, scale):
        return (head, len(tail), tail[0], scale)

    @staticmethod
    def defaulted(head=seed, *tail, scale=2, offset=1):
        return head * scale + len(tail) + offset

    @staticmethod
    def only(*items, scale):
        return (len(items), scale)

    @classmethod
    def tag(cls, head, *tail, scale):
        return cls.kind + head * scale + len(tail)

    @classmethod
    def defaulted_tag(cls, head=seed, *tail, scale=2, offset=1):
        return cls.kind + head * scale + len(tail) + offset

    seed = 50


class MoreTools(Tools):
    kind = 100


staticmethod_ok = (
    Tools.mix(2, 3, 4, scale=5) == (2, 2, 3, 5)
    and Tools.defaulted(offset=3) == 13
    and Tools.defaulted(4, 8, 9, scale=3, offset=1) == 15
    and Tools.only(1, 2, scale=7) == (2, 7)
    and Tools().only(scale=6) == (0, 6)
)

classmethod_ok = (
    Tools.tag(2, 3, 4, scale=5) == 22
    and MoreTools.tag(2, 3, scale=4) == 109
    and Tools.defaulted_tag(offset=4) == 24
    and MoreTools.defaulted_tag(3, 4, 5, scale=2) == 109
    and getattr(MoreTools(), "tag")(1, 2, 3, scale=4) == 106
)


def identity(cls):
    return cls


@identity
class Decorated:
    seed = 3

    def calc(self, value=seed, *items, scale=2):
        return value * scale + len(items)


@identity
class DecoratedChild(Decorated):
    def add(self, value, *items, scale, offset=1):
        return self.calc(value, *items, scale=scale) + offset


decorated_ok = (
    Decorated().calc(scale=4) == 12
    and Decorated().calc(2, 5, 6, scale=3) == 8
    and DecoratedChild().add(2, 5, 6, scale=3, offset=4) == 12
)

missing_plain_kw = False
try:
    c.pack("x", 1, 2)
except TypeError:
    missing_plain_kw = True

duplicate_plain = False
try:
    c.pack("x", label="y", scale=2)
except TypeError:
    duplicate_plain = True

unknown_plain = False
try:
    c.only(scale=2, extra=3)
except TypeError:
    unknown_plain = True

missing_static_kw = False
try:
    Tools.only(1)
except TypeError:
    missing_static_kw = True

missing_class_kw = False
try:
    Tools.tag(1)
except TypeError:
    missing_class_kw = True

errors_ok = (
    missing_plain_kw
    and duplicate_plain
    and unknown_plain
    and missing_static_kw
    and missing_class_kw
)

result = plain_ok and staticmethod_ok and classmethod_ok and decorated_ok and errors_ok
assert result
result
