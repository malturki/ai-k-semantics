result = True


class Collector:
    def __init__(self, *items):
        self.count = len(items)

    def pack(self, label, *items):
        return (label, len(items), items[0], items[1])

    def empty(self, *items):
        return items == ()


class Child(Collector):
    pass


c = Collector(4, 5, 6)
result = result and c.count == 3
result = result and c.pack("x", 1, 2) == ("x", 2, 1, 2)
result = result and Collector.pack(c, "y", 3, 4) == ("y", 2, 3, 4)
result = result and getattr(c, "pack")("z", 8, 9) == ("z", 2, 8, 9)
result = result and c.empty()

child = Child(1)
result = result and child.pack("c", 2, 3) == ("c", 2, 2, 3)


class Tools:
    kind = 10

    @staticmethod
    def count(*items):
        return len(items)

    @staticmethod
    def first(label, *items):
        return (label, items[0], len(items))

    @classmethod
    def tagged(cls, *items):
        return cls.kind + len(items)


class MoreTools(Tools):
    kind = 20


result = result and Tools.count() == 0
result = result and Tools.count(1, 2, 3) == 3
result = result and Tools().count(1, 2) == 2
result = result and Tools.first("a", 4, 5) == ("a", 4, 2)
result = result and Tools.tagged(1, 2) == 12
result = result and MoreTools.tagged(1, 2, 3) == 23
result = result and getattr(MoreTools(), "tagged")(4) == 21

missing = False
try:
    c.pack()
except TypeError:
    missing = True
result = result and missing

result
