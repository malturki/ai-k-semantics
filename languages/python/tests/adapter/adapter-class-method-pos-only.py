class Worker:
    base = 4

    def __init__(self, start=base, /, extra=1):
        self.total = start + extra

    def add(self, value=base, /, scale=2):
        return self.total + value * scale

    def required(self, value, /, scale=1):
        return self.total + value * scale

    def bare(self, value, /):
        return self.total + value

    base = 40


class Child(Worker):
    pass


class Tools:
    seed = 5
    kind = 10

    @staticmethod
    def mix(value=seed, /, scale=2):
        return value * scale

    @staticmethod
    def required(value, /, scale=1):
        return value + scale

    @staticmethod
    def only(value, /):
        return value + 1

    @classmethod
    def tag(cls, value=seed, /, scale=2):
        return cls.kind + value * scale

    @classmethod
    def req(cls, value, /, scale=1):
        return cls.kind + value + scale

    @classmethod
    def bare(cls, value, /):
        return cls.kind + value

    seed = 50


class MoreTools(Tools):
    kind = 100


w = Worker(10, extra=3)
defaulted = Worker(extra=2)
child = Child(7, extra=1)

plain_ok = (
    w.total == 13
    and defaulted.total == 6
    and w.add(2, scale=3) == 19
    and w.add(scale=5) == 33
    and Worker.add(w, 3, scale=4) == 25
    and getattr(w, "add")(5) == 23
    and child.add(1, scale=2) == 10
    and defaulted.add(scale=2) == 14
    and Worker.required(w, 2, scale=5) == 23
    and w.required(3) == 16
    and w.bare(5) == 18
    and Worker.bare(w, 6) == 19
)

staticmethod_ok = (
    Tools.mix() == 10
    and Tools.mix(3, scale=4) == 12
    and Tools.required(4, scale=6) == 10
    and Tools.only(4) == 5
)

classmethod_ok = (
    Tools.tag() == 20
    and MoreTools.tag(2, scale=3) == 106
    and Tools.req(1, scale=2) == 13
    and MoreTools.req(1, scale=2) == 103
    and MoreTools.bare(7) == 107
)

missing_direct = False
try:
    Worker.required(scale=2)
except TypeError:
    missing_direct = True

keyword_plain = False
try:
    w.required(value=2)
except TypeError:
    keyword_plain = True

duplicate_plain = False
try:
    w.required(2, value=3)
except TypeError:
    duplicate_plain = True

keyword_static = False
try:
    Tools.mix(value=1)
except TypeError:
    keyword_static = True

missing_static = False
try:
    Tools.required(scale=1)
except TypeError:
    missing_static = True

keyword_class = False
try:
    Tools.tag(value=1)
except TypeError:
    keyword_class = True

missing_class = False
try:
    Tools.req(scale=1)
except TypeError:
    missing_class = True

errors_ok = (
    missing_direct
    and keyword_plain
    and duplicate_plain
    and keyword_static
    and missing_static
    and keyword_class
    and missing_class
)

result = plain_ok and staticmethod_ok and classmethod_ok and errors_ok
assert result
result
