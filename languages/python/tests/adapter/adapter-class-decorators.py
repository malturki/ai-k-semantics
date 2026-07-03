result = True


class Replacement:
    tag = 99


class ReplacementA:
    tag = 10


class ReplacementB:
    tag = 20


class ReplacementC:
    tag = 30


def identity(cls):
    return cls


def replace(cls):
    return Replacement


def make_replace():
    return replace


def to_a(cls):
    return ReplacementA


def choose(cls):
    if cls is ReplacementA:
        return ReplacementB
    return ReplacementC


@identity
class Kept:
    tag = 1


@replace
class Replaced:
    tag = 2


@make_replace()
class ReplacedByFactory:
    tag = 3


@choose
@to_a
class Ordered:
    tag = 4


class Base:
    base = 5

    def __init__(self, value):
        self.value = value

    def total(self):
        return self.value + self.base


@identity
class Child(Base):
    base = 7
    extra = 8

    def total(self):
        return Base.total(self) + self.extra


k = Kept()
c = Child(10)

result = result and Kept.tag == 1
result = result and isinstance(k, Kept)
result = result and Replaced is Replacement
result = result and Replaced.tag == 99
result = result and ReplacedByFactory is Replacement
result = result and Ordered is ReplacementB
result = result and Ordered.tag == 20
result = result and isinstance(c, Child)
result = result and isinstance(c, Base)
result = result and c.total() == 25
result = result and Child.total(c) == 25
result = result and Base.total(c) == 17

assert result
result
