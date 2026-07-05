async def coro(value):
    "async doc"
    return value


async def empty():
    pass


result = (
    callable(coro)
    and callable(empty)
    and coro.__name__ == "coro"
    and coro.__qualname__ == "coro"
    and coro.__module__ == "__main__"
    and coro.__doc__ == "async doc"
    and empty.__doc__ is None
)

result
