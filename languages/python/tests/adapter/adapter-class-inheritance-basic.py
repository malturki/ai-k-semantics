result = True


class Base:
    kind = 1
    shared = 10

    def __init__(self, value):
        self.value = value

    def total(self):
        return self.value + self.shared

    def label(self):
        return self.kind


class Child(Base):
    kind = 2
    extra = 5

    def bump(self, amount):
        self.value = self.value + amount
        return self.value

    def total(self):
        return Base.total(self) + self.extra


class GrandChild(Child):
    pass


class Other:
    pass


c = Child(7)
g = GrandChild(3)

result = result and c.value == 7
result = result and c.kind == 2
result = result and c.shared == 10
result = result and c.extra == 5
result = result and c.label() == 2
result = result and c.total() == 22
result = result and Child.total(c) == 22
result = result and Base.total(c) == 17
result = result and c.bump(4) == 11
result = result and c.total() == 26
result = result and isinstance(c, Child)
result = result and isinstance(c, Base)
result = result and not isinstance(c, Other)
result = result and isinstance(g, GrandChild)
result = result and isinstance(g, Child)
result = result and isinstance(g, Base)
result = result and issubclass(Child, Base)
result = result and issubclass(GrandChild, Base)
result = result and not issubclass(Base, Child)
result = result and not issubclass(Other, Base)
result = result and getattr(c, "shared") == 10
result = result and callable(getattr(c, "label"))
result = result and hasattr(c, "label")
result = result and not hasattr(c, "missing")

assert result
result
