class Worker:
    base = 3

    def __init__(self, start=base, *, extra, scale=2):
        self.total = (start + extra) * scale

    def add(self, value=base, *, scale, offset=1):
        return self.total + value * scale + offset

    def required(self, *, value, scale=1):
        return self.total + value * scale

    def pure(self, value, *, scale):
        return self.total + value * scale

    base = 30


class Child(Worker):
    pass


w = Worker(extra=4)
w2 = Worker(5, extra=2, scale=3)
child = Child(extra=1)

plain_ok = (
    w.total == 14
    and w2.total == 21
    and child.total == 8
    and w.add(scale=2) == 21
    and w.add(4, scale=3, offset=2) == 28
    and Worker.add(w, scale=1) == 18
    and Worker.pure(w, 2, scale=5) == 24
    and getattr(w, "required")(value=5, scale=2) == 24
    and getattr(w, "pure")(2, scale=3) == 20
    and child.add(scale=1) == 12
    and child.pure(3, scale=2) == 14
    and w2.required(value=2) == 23
)


class Tools:
    seed = 5
    kind = 10

    @staticmethod
    def mix(value=seed, *, scale, offset=1):
        return value * scale + offset

    @staticmethod
    def only(*, value, scale=2):
        return value * scale

    @staticmethod
    def needed(*, value):
        return value + 1

    @staticmethod
    def pair(value, *, scale):
        return value * scale

    @classmethod
    def tag(cls, value=seed, *, scale, offset=1):
        return cls.kind + value * scale + offset

    @classmethod
    def req(cls, *, value, scale=1):
        return cls.kind + value * scale

    @classmethod
    def mark(cls, value, *, scale):
        return cls.kind + value * scale

    seed = 50


class MoreTools(Tools):
    kind = 100


staticmethod_ok = (
    Tools.mix(scale=3) == 16
    and Tools.mix(4, scale=2, offset=3) == 11
    and Tools.only(value=6) == 12
    and Tools.needed(value=8) == 9
    and Tools.pair(7, scale=3) == 21
    and Tools().only(value=3, scale=4) == 12
    and Tools().needed(value=5) == 6
)

classmethod_ok = (
    Tools.tag(scale=2) == 21
    and MoreTools.tag(3, scale=4, offset=5) == 117
    and Tools.req(value=7) == 17
    and Tools.mark(4, scale=2) == 18
    and MoreTools.req(value=2, scale=5) == 110
    and MoreTools.mark(3, scale=5) == 115
    and getattr(MoreTools(), "req")(value=1) == 101
    and getattr(MoreTools(), "mark")(2, scale=6) == 112
)

missing_plain = False
try:
    w.add()
except TypeError:
    missing_plain = True

positional_plain = False
try:
    w.required(1, value=2)
except TypeError:
    positional_plain = True

missing_static = False
try:
    Tools.only()
except TypeError:
    missing_static = True

positional_static = False
try:
    Tools.only(2)
except TypeError:
    positional_static = True

missing_static_required = False
try:
    Tools.needed()
except TypeError:
    missing_static_required = True

positional_static_required = False
try:
    Tools.needed(2)
except TypeError:
    positional_static_required = True

missing_class = False
try:
    Tools.req()
except TypeError:
    missing_class = True

positional_class = False
try:
    Tools.req(2, value=3)
except TypeError:
    positional_class = True

missing_class_required = False
try:
    Tools.mark(2)
except TypeError:
    missing_class_required = True

errors_ok = (
    missing_plain
    and positional_plain
    and missing_static
    and positional_static
    and missing_static_required
    and positional_static_required
    and missing_class
    and positional_class
    and missing_class_required
)

result = plain_ok and staticmethod_ok and classmethod_ok and errors_ok
assert result
result
