result = True


class Collector:
    base = 5

    def __init__(self, start=base, **kw):
        self.total = start + len(kw) + kw["bonus"]

    def score(self, value, **kw):
        return self.total + value * 10 + len(kw) + kw["bonus"]

    def default_score(self, value=base, **kw):
        return value + len(kw) + kw["bonus"]

    base = 50


class Child(Collector):
    pass


c = Collector(bonus=4, extra=9)
explicit = Collector(3, bonus=2)
child = Child(bonus=1)

result = result and c.total == 11
result = result and explicit.total == 6
result = result and child.total == 7
result = result and c.score(2, bonus=3) == 35
result = result and c.score(2, bonus=3, extra=4) == 36
result = result and Collector.score(c, 4, bonus=1) == 53
result = result and getattr(c, "score")(1, bonus=8) == 30
result = result and c.default_score(bonus=6) == 12
result = result and c.default_score(7, bonus=6, extra=0) == 15
result = result and Collector.base == 50
result = result and child.score(1, bonus=2) == 20


class Tools:
    seed = 10
    kind = 100

    @staticmethod
    def tally(**kw):
        return len(kw) + kw["x"]

    @staticmethod
    def default_tally(value=seed, **kw):
        return value + len(kw) + kw["bonus"]

    @classmethod
    def tagged(cls, value=seed, **kw):
        return cls.kind + value + len(kw) + kw["bonus"]

    @classmethod
    def only_kw(cls, **kw):
        return cls.kind + len(kw) + kw["bonus"]


class MoreTools(Tools):
    kind = 200


result = result and Tools.tally(x=4) == 5
result = result and Tools.tally(x=4, y=5) == 6
result = result and Tools().tally(x=6) == 7
result = result and Tools.default_tally(bonus=3) == 14
result = result and Tools.default_tally(7, bonus=3, extra=1) == 12
result = result and Tools.tagged(bonus=5) == 116
result = result and Tools().tagged(2, bonus=5) == 108
result = result and MoreTools.tagged(bonus=5) == 216
result = result and MoreTools().only_kw(bonus=7, extra=0) == 209
result = result and getattr(MoreTools(), "only_kw")(bonus=1) == 202

missing = False
try:
    c.score(bonus=1)
except TypeError:
    missing = True

too_many = False
try:
    c.score(1, 2, bonus=3)
except TypeError:
    too_many = True

result = result and missing
result = result and too_many

assert result
result
