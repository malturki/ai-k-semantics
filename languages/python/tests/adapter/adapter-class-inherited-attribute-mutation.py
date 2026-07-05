result = True


class Base:
    live = 1
    inherited_delete = 8
    base_only = 11


class Child(Base):
    pass


class GrandChild(Child):
    pass


c = Child()
g = GrandChild()

result = result and Base.live == 1
result = result and Child.live == 1
result = result and GrandChild.live == 1
result = result and c.live == 1
result = result and g.live == 1

Base.live = 2
result = result and Base.live == 2
result = result and Child.live == 2
result = result and GrandChild.live == 2
result = result and c.live == 2
result = result and g.live == 2
result = result and Child().live == 2
result = result and GrandChild().live == 2

Child.live = 3
result = result and Base.live == 2
result = result and Child.live == 3
result = result and GrandChild.live == 3
result = result and c.live == 3
result = result and g.live == 3

Base.live = 4
result = result and Base.live == 4
result = result and Child.live == 3
result = result and GrandChild.live == 3
result = result and c.live == 3
result = result and g.live == 3

del Child.live
result = result and Base.live == 4
result = result and Child.live == 4
result = result and GrandChild.live == 4
result = result and c.live == 4
result = result and g.live == 4

try:
    del Child.inherited_delete
    result = False
except AttributeError:
    result = result and Child.inherited_delete == 8
    result = result and c.inherited_delete == 8

del Base.inherited_delete
result = result and not hasattr(Base, "inherited_delete")
result = result and not hasattr(Child, "inherited_delete")
result = result and not hasattr(GrandChild, "inherited_delete")
result = result and not hasattr(c, "inherited_delete")
result = result and not hasattr(g, "inherited_delete")

setattr(Base, "base_only", 12)
result = result and Base.base_only == 12
result = result and Child.base_only == 12
result = result and GrandChild.base_only == 12
result = result and getattr(c, "base_only") == 12
result = result and getattr(g, "base_only") == 12

setattr(Child, "base_only", 13)
result = result and Base.base_only == 12
result = result and Child.base_only == 13
result = result and GrandChild.base_only == 13
result = result and c.base_only == 13
result = result and g.base_only == 13

delattr(Child, "base_only")
result = result and Base.base_only == 12
result = result and Child.base_only == 12
result = result and GrandChild.base_only == 12
result = result and c.base_only == 12
result = result and g.base_only == 12

delattr(Base, "base_only")
result = result and getattr(Base, "base_only", 21) == 21
result = result and getattr(Child, "base_only", 22) == 22
result = result and getattr(GrandChild, "base_only", 23) == 23
result = result and getattr(c, "base_only", 24) == 24
result = result and getattr(g, "base_only", 25) == 25

result
