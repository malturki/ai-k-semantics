result = True


def plain(a):
    "plain doc"
    return a + 1


def empty():
    pass


def no_doc(x, y=2):
    return x + y


result = result and plain.__name__ == "plain"
result = result and plain.__qualname__ == "plain"
result = result and plain.__module__ == "__main__"
result = result and plain.__doc__ == "plain doc"
result = result and getattr(plain, "__name__") == "plain"
result = result and getattr(plain, "__doc__") == "plain doc"
result = result and hasattr(plain, "__qualname__")
result = result and plain(2) == 3
result = result and empty.__doc__ is None and empty() is None
result = result and no_doc.__doc__ is None and no_doc(3) == 5

assert result
result
