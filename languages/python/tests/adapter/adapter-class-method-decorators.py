result = True


class Base:
    kind = 1

    def __init__(self, value):
        self.value = value

    @staticmethod
    def add(left, right):
        return left + right

    @classmethod
    def tag(cls, extra):
        return cls.kind + extra

    @classmethod
    def make(cls, value):
        return cls(value)


class Child(Base):
    kind = 10


b = Base.make(7)
c = Child.make(8)

result = result and isinstance(b, Base)
result = result and not isinstance(b, Child)
result = result and isinstance(c, Child)
result = result and isinstance(c, Base)
result = result and b.value == 7
result = result and c.value == 8
result = result and Base.add(2, 3) == 5
result = result and b.add(4, 5) == 9
result = result and Child.add(6, 7) == 13
result = result and c.add(8, 9) == 17
result = result and Base.tag(4) == 5
result = result and b.tag(4) == 5
result = result and Child.tag(4) == 14
result = result and c.tag(4) == 14
result = result and getattr(c, "tag")(1) == 11
result = result and getattr(Child, "add")(6, 7) == 13
result = result and callable(getattr(c, "tag"))
result = result and callable(getattr(Base, "add"))

assert result
result
