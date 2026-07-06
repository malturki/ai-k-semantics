result = True


class Base:
    flag = 1
    gone = 9


class Child(Base):
    pass


classes = [Base, Child]
instances = [Base(), Child()]
pair = (Base, Child, Base(), Child())
mapping = {"base": Base, "child": Child, "base_instance": Base(), "child_instance": Child()}
nested = [[Base], {"base": Base, "child": Child, "instance": Base()}]

classes[0].flag = 2
result = result and Base.flag == 2
result = result and Child.flag == 2
result = result and classes[0].flag == 2
result = result and classes[1].flag == 2
result = result and instances[0].flag == 2
result = result and instances[1].flag == 2
result = result and pair[0].flag == 2
result = result and pair[1].flag == 2
result = result and pair[2].flag == 2
result = result and pair[3].flag == 2
result = result and mapping["base"].flag == 2
result = result and mapping["child"].flag == 2
result = result and mapping["base_instance"].flag == 2
result = result and mapping["child_instance"].flag == 2
result = result and nested[0][0].flag == 2
result = result and nested[1]["base"].flag == 2
result = result and nested[1]["child"].flag == 2
result = result and nested[1]["instance"].flag == 2

setattr(pair[1], "flag", 3)
result = result and Base.flag == 2
result = result and Child.flag == 3
result = result and classes[1].flag == 3
result = result and instances[1].flag == 3
result = result and pair[1].flag == 3
result = result and pair[3].flag == 3
result = result and mapping["child"].flag == 3
result = result and mapping["child_instance"].flag == 3
result = result and nested[1]["child"].flag == 3

Base.flag = 4
result = result and Base.flag == 4
result = result and Child.flag == 3
result = result and classes[0].flag == 4
result = result and classes[1].flag == 3
result = result and instances[0].flag == 4
result = result and instances[1].flag == 3
result = result and pair[0].flag == 4
result = result and pair[1].flag == 3
result = result and pair[2].flag == 4
result = result and pair[3].flag == 3
result = result and mapping["base"].flag == 4
result = result and mapping["child"].flag == 3
result = result and mapping["base_instance"].flag == 4
result = result and mapping["child_instance"].flag == 3
result = result and nested[0][0].flag == 4
result = result and nested[1]["base"].flag == 4
result = result and nested[1]["child"].flag == 3
result = result and nested[1]["instance"].flag == 4

delattr(classes[1], "flag")
result = result and Child.flag == 4
result = result and classes[1].flag == 4
result = result and instances[1].flag == 4
result = result and pair[1].flag == 4
result = result and pair[3].flag == 4
result = result and mapping["child"].flag == 4
result = result and mapping["child_instance"].flag == 4
result = result and nested[1]["child"].flag == 4

setattr(nested[0][0], "extra", 5)
result = result and Base.extra == 5
result = result and Child.extra == 5
result = result and classes[0].extra == 5
result = result and classes[1].extra == 5
result = result and instances[0].extra == 5
result = result and instances[1].extra == 5
result = result and pair[2].extra == 5
result = result and pair[3].extra == 5
result = result and mapping["base"].extra == 5
result = result and mapping["child"].extra == 5
result = result and nested[1]["instance"].extra == 5

del mapping["base"].gone
result = result and not hasattr(Base, "gone")
result = result and not hasattr(Child, "gone")
result = result and not hasattr(classes[0], "gone")
result = result and not hasattr(classes[1], "gone")
result = result and not hasattr(instances[0], "gone")
result = result and not hasattr(instances[1], "gone")
result = result and not hasattr(pair[2], "gone")
result = result and not hasattr(pair[3], "gone")
result = result and not hasattr(mapping["base_instance"], "gone")
result = result and not hasattr(mapping["child_instance"], "gone")
result = result and not hasattr(nested[1]["instance"], "gone")

delattr(nested[1]["base"], "extra")
result = result and getattr(Base, "extra", 11) == 11
result = result and getattr(Child, "extra", 12) == 12
result = result and getattr(classes[0], "extra", 13) == 13
result = result and getattr(classes[1], "extra", 14) == 14
result = result and getattr(instances[0], "extra", 15) == 15
result = result and getattr(instances[1], "extra", 16) == 16
result = result and getattr(mapping["base_instance"], "extra", 17) == 17
result = result and getattr(mapping["child_instance"], "extra", 18) == 18

result
