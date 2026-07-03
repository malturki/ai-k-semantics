result = True


class Counter:
    base = 10

    def __init__(self, start=base):
        self.value = start

    def bump(self, amount=1):
        self.value = self.value + amount
        return self.value

    def scale(self, factor=base):
        return self.value * factor


class Child(Counter):
    def bump(self, amount=2):
        return Counter.bump(self, amount)


class DefaultScope:
    seed = 5

    def get(self, value=seed):
        return value

    seed = 20


class Tools:
    seed = 4
    kind = 100

    @staticmethod
    def add(left=seed, right=3):
        return left + right

    @classmethod
    def tag(cls, extra=seed):
        return cls.kind + extra


class MoreTools(Tools):
    kind = 200


c = Counter()
explicit = Counter(7)
child = Child()
scope = DefaultScope()

result = result and c.value == 10
result = result and c.bump() == 11
result = result and c.bump(4) == 15
result = result and c.scale() == 150
result = result and c.scale(2) == 30
result = result and explicit.value == 7
result = result and explicit.scale() == 70
result = result and Counter.scale(explicit) == 70
result = result and getattr(c, "bump")() == 16
result = result and child.value == 10
result = result and child.bump() == 12
result = result and child.bump(5) == 17
result = result and scope.get() == 5
result = result and DefaultScope.seed == 20
result = result and Tools.add() == 7
result = result and Tools.add(8) == 11
result = result and Tools.add(8, 9) == 17
result = result and Tools().add() == 7
result = result and getattr(Tools, "add")() == 7
result = result and Tools.tag() == 104
result = result and Tools().tag() == 104
result = result and MoreTools.tag() == 204
result = result and MoreTools().tag(6) == 206
result = result and getattr(MoreTools(), "tag")() == 204

too_many = False
try:
    c.bump(1, 2)
except TypeError:
    too_many = True

result = result and too_many

assert result
result
