result = True

def identity(cls):
    return cls

class Collector:
    seed = 4

    def __init__(self, start=seed, *items, scale, offset=1, **kw):
        self.total = (start + len(items) + kw["bonus"]) * scale + offset + len(kw)

    def pack(self, label, *items, scale, **kw):
        return (label, self.total * scale, len(items), kw["tag"], len(kw))

    def defaulted(self, value=seed, *items, scale=2, offset=1, **kw):
        return self.total + value * scale + len(items) + offset + kw["bonus"] + len(kw)

    def only(self, *items, scale, **kw):
        return (self.total, len(items), scale, kw["bonus"], len(kw))

    seed = 40

class Child(Collector):
    pass

c = Collector(1, 2, 3, scale=2, bonus=4, extra=9)
defaulted = Collector(scale=3, bonus=1)
child = Child(2, 9, scale=2, bonus=1)

plain_ok = (
    c.total == 17
    and defaulted.total == 17
    and child.total == 10
    and c.pack("p", 5, 6, scale=3, tag="ok", spare=1) == ("p", 51, 2, "ok", 2)
    and Collector.pack(c, "q", 7, 8, scale=1, tag="direct") == ("q", 17, 2, "direct", 1)
    and defaulted.defaulted(bonus=5) == 32
    and c.defaulted(2, 9, 10, scale=3, offset=4, bonus=5, extra=0) == 36
    and child.only(1, 2, 3, scale=4, bonus=2, extra=8) == (10, 3, 4, 2, 2)
)

class Tools:
    seed = 5
    kind = 10

    @staticmethod
    def mix(head, *tail, scale, **kw):
        return (head, len(tail), tail[0], scale, kw["bonus"], len(kw))

    @staticmethod
    def defaulted(head=seed, *tail, scale=2, offset=1, **kw):
        return head * scale + len(tail) + offset + kw["bonus"] + len(kw)

    @staticmethod
    def only(*items, scale, **kw):
        return (len(items), scale, kw["bonus"], len(kw))

    @classmethod
    def tag(cls, head, *tail, scale, **kw):
        return cls.kind + head * scale + len(tail) + kw["bonus"] + len(kw)

    @classmethod
    def defaulted_tag(cls, head=seed, *tail, scale=2, offset=1, **kw):
        return cls.kind + head * scale + len(tail) + offset + kw["bonus"] + len(kw)

    seed = 50

class MoreTools(Tools):
    kind = 100

staticmethod_ok = (
    Tools.mix(2, 3, 4, scale=5, bonus=6, extra=1) == (2, 2, 3, 5, 6, 2)
    and Tools.defaulted(offset=3, bonus=4) == 18
    and Tools.defaulted(4, 8, 9, scale=3, offset=1, bonus=2, extra=7) == 19
    and Tools.only(1, 2, scale=7, bonus=8) == (2, 7, 8, 1)
    and Tools().only(scale=6, bonus=2, extra=0) == (0, 6, 2, 2)
)

classmethod_ok = (
    Tools.tag(2, 3, 4, scale=5, bonus=6) == 29
    and MoreTools.tag(2, 3, scale=4, bonus=5, extra=1) == 116
    and Tools.defaulted_tag(offset=4, bonus=5) == 30
    and MoreTools.defaulted_tag(3, 4, 5, scale=2, bonus=1) == 111
    and getattr(MoreTools(), "tag")(1, 2, 3, scale=4, bonus=5, marker=9) == 113
)

@identity
class Decorated:
    seed = 3

    def calc(self, value=seed, *items, scale=2, **kw):
        return value * scale + len(items) + kw["bonus"] + len(kw)

@identity
class DecoratedChild(Decorated):
    def add(self, value, *items, scale, offset=1, **kw):
        return value * scale + len(items) + offset + kw["bonus"] + len(kw)

decorated_ok = (
    Decorated().calc(scale=4, bonus=2) == 15
    and Decorated().calc(2, 5, 6, scale=3, bonus=4, extra=1) == 14
    and DecoratedChild().add(2, 5, 6, scale=3, offset=4, bonus=7, extra=1) == 21
)

missing_plain_kw = False
try:
    c.pack("x", 1, 2, tag="bad")
except TypeError:
    missing_plain_kw = True

duplicate_plain = False
try:
    c.pack("x", 1, label="dup", scale=2, tag="ok")
except TypeError:
    duplicate_plain = True

missing_static_kw = False
try:
    Tools.only(1, 2, bonus=1)
except TypeError:
    missing_static_kw = True

duplicate_static = False
try:
    Tools.mix(2, 3, head=4, scale=1, bonus=1)
except TypeError:
    duplicate_static = True

missing_class_kw = False
try:
    Tools.tag(1, bonus=1)
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
