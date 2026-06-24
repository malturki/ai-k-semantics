def plain():
    return None


def with_args(x, y=1, *args, scale=2, **kw):
    return x


lambda_two = lambda x, y: x + y
lambda_var = lambda *args, **kw: 1

result = callable(plain)
result = result and callable(with_args)
result = result and callable(lambda_two)
result = result and callable(lambda_var)

result = result and not callable("a")
result = result and not callable(0)
result = result and not callable(True)
result = result and not callable(None)
result = result and not callable([])
result = result and not callable(())
result = result and not callable({})
result = result and not callable(set())

assert result
result
