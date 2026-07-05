result = True


class Mutable:
    x = 1

    def value(self):
        return self.x


c = Mutable()
Alias = Mutable

result = result and Mutable.x == 1
result = result and Alias.x == 1
result = result and c.x == 1
result = result and c.value() == 1

Mutable.x = 2
result = result and Mutable.x == 2
result = result and Alias.x == 2
result = result and c.x == 2
result = result and c.value() == 2
result = result and Mutable().x == 2

Alias.y = 3
result = result and Mutable.y == 3
result = result and Alias.y == 3
result = result and c.y == 3
result = result and getattr(Mutable, "y") == 3
result = result and getattr(c, "y") == 3
result = result and hasattr(Mutable, "y")
result = result and hasattr(c, "y")

result = result and setattr(Mutable, "z", 4) is None
result = result and Mutable.z == 4
result = result and Alias.z == 4
result = result and c.z == 4
result = result and getattr(Alias, "z") == 4
result = result and getattr(c, "z") == 4

c.own = 9
Mutable.own = 10
result = result and Mutable.own == 10
result = result and c.own == 9
result = result and getattr(c, "own") == 9

del Alias.y
result = result and not hasattr(Mutable, "y")
result = result and not hasattr(c, "y")
result = result and getattr(Mutable, "y", 30) == 30
result = result and getattr(c, "y", 40) == 40

result = result and delattr(Mutable, "z") is None
result = result and not hasattr(Alias, "z")
result = result and not hasattr(c, "z")
result = result and getattr(Alias, "z", 50) == 50
result = result and getattr(c, "z", 60) == 60

del Mutable.own
result = result and not hasattr(Mutable, "own")
result = result and c.own == 9

try:
    del Mutable.missing
    result = False
except AttributeError:
    result = result and True

try:
    delattr(Mutable, "missing")
    result = False
except AttributeError:
    result = result and True

result
