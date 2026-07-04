result = True


class Collector:
    base = 5

    def __init__(self, start=base, *items, **kw):
        self.total = start + len(items) + len(kw) + kw["bonus"]

    def score(self, value=base, *items, **kw):
        return self.total + value * 10 + len(items) + len(kw) + kw["bonus"]

    def required(self, value, *items, **kw):
        return self.total + value + len(items) + len(kw) + kw["bonus"]

    base = 50


class Child(Collector):
    pass


c = Collector(1, 2, 3, bonus=4, extra=9)
defaulted = Collector(bonus=1)
child = Child(bonus=2, more=3)

result = result and c.total == 9
result = result and defaulted.total == 7
result = result and child.total == 9
result = result and c.score(bonus=6) == 66
result = result and c.score(2, 3, 4, bonus=5, extra=6) == 38
result = result and c.score(value=2, bonus=3) == 33
result = result and c.required(2, 3, bonus=4, extra=5) == 18
result = result and Collector.score(c, 7, 8, bonus=9) == 90
result = result and getattr(c, "score")(1, 2, bonus=3) == 24
result = result and Collector.base == 50
result = result and child.score(bonus=3) == 63


class Tools:
    seed = 10
    kind = 100

    @staticmethod
    def mix(value=seed, *items, **kw):
        return value + len(items) + len(kw) + kw["bonus"]

    @staticmethod
    def only(*items, **kw):
        return len(items) + len(kw) + kw["x"]

    @classmethod
    def tagged(cls, value=seed, *items, **kw):
        return cls.kind + value + len(items) + len(kw) + kw["bonus"]

    @classmethod
    def collect(cls, *items, **kw):
        return cls.kind + len(items) + len(kw) + kw["bonus"]


class MoreTools(Tools):
    kind = 200


result = result and Tools.mix(bonus=3) == 14
result = result and Tools.mix(7, 8, 9, bonus=3, extra=1) == 14
result = result and Tools().mix(bonus=4) == 15
result = result and getattr(Tools, "mix")(1, 2, bonus=3) == 6
result = result and Tools.only(1, 2, x=5, y=6) == 9
result = result and Tools.tagged(bonus=5) == 116
result = result and Tools().tagged(2, 3, bonus=5, extra=0) == 110
result = result and MoreTools.tagged(bonus=6) == 217
result = result and getattr(MoreTools(), "collect")(1, 2, bonus=3, z=0) == 207

missing_receiver = False
try:
    Collector.required(bonus=1)
except TypeError:
    missing_receiver = True

missing_value = False
try:
    c.required(bonus=1)
except TypeError:
    missing_value = True

duplicate_required = False
try:
    c.required(1, value=2, bonus=3)
except TypeError:
    duplicate_required = True

duplicate_defaulted = False
try:
    c.score(1, value=2, bonus=3)
except TypeError:
    duplicate_defaulted = True

result = result and missing_receiver
result = result and missing_value
result = result and duplicate_required
result = result and duplicate_defaulted

assert result
result
