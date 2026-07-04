result = True


class Collector:
    seed = 5

    def __init__(self, start=seed, *items):
        self.total = start + len(items)

    def score(self, value=seed, *items):
        return self.total + value * 10 + len(items)

    seed = 50


class Child(Collector):
    pass


c = Collector(1, 2, 3)
defaulted = Collector()
child = Child()

result = result and c.total == 3
result = result and defaulted.total == 5
result = result and child.total == 5
result = result and c.score() == 53
result = result and c.score(2, 3, 4) == 25
result = result and Collector.score(c) == 53
result = result and getattr(c, "score")(7, 8) == 74
result = result and Collector.seed == 50
result = result and child.score(1, 2) == 16


class Tools:
    seed = 10
    kind = 100

    @staticmethod
    def add(value=seed, *items):
        return value + len(items)

    @classmethod
    def tagged(cls, value=seed, *items):
        return cls.kind + value + len(items)


class MoreTools(Tools):
    kind = 200


result = result and Tools.add() == 10
result = result and Tools.add(3, 4, 5) == 5
result = result and Tools().add() == 10
result = result and getattr(Tools, "add")(7, 8) == 8
result = result and Tools.tagged() == 110
result = result and Tools().tagged(3, 4) == 104
result = result and MoreTools.tagged(1, 2, 3) == 203
result = result and getattr(MoreTools(), "tagged")() == 210

missing_self = False
try:
    Collector.score()
except TypeError:
    missing_self = True

duplicate = False
try:
    c.score(1, value=2)
except TypeError:
    duplicate = True

unknown_keyword = False
try:
    c.score(extra=1)
except TypeError:
    unknown_keyword = True

result = result and missing_self
result = result and duplicate
result = result and unknown_keyword

assert result
result
