result = True


class Empty:
    pass


class Documented:
    "documented class"
    marker = __doc__
    module_name = __module__
    qual_name = __qualname__


class Override:
    "first"
    __doc__ = "second"
    __module__ = "custom.module"
    __qualname__ = "CustomName"


def identity(cls):
    return cls


@identity
class Decorated:
    "decorated class"


class Child(Documented):
    "child class"


result = result and Empty.__doc__ is None
result = result and Empty.__module__ == "__main__"
result = result and Empty.__qualname__ == "Empty"
result = result and Documented.__doc__ == "documented class"
result = result and Documented.marker == "documented class"
result = result and Documented.module_name == "__main__"
result = result and Documented.qual_name == "Documented"
result = result and getattr(Documented, "__doc__") == "documented class"
result = result and getattr(Documented, "__module__") == "__main__"
result = result and getattr(Documented, "__qualname__") == "Documented"
result = result and hasattr(Documented, "__doc__")
result = result and hasattr(Documented, "__module__")
result = result and hasattr(Documented, "__qualname__")
result = result and Override.__doc__ == "second"
result = result and Override.__module__ == "custom.module"
result = result and Override.__qualname__ == "CustomName"
result = result and Decorated.__doc__ == "decorated class"
result = result and Decorated.__module__ == "__main__"
result = result and Decorated.__qualname__ == "Decorated"
result = result and Child.__doc__ == "child class"
result = result and Child.__module__ == "__main__"
result = result and Child.__qualname__ == "Child"

assert result
result
