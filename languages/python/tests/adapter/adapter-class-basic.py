result = True


class Simple:
    pass


class Other:
    pass


result = result and callable(Simple)
result = result and bool(Simple)

a = Simple()
b = Simple()
alias = a
ClassAlias = Simple

result = result and bool(a)
result = result and isinstance(a, Simple)
result = result and isinstance(b, Simple)
result = result and not isinstance(a, Other)
result = result and a is alias
result = result and a is not b
result = result and a == alias
result = result and a != b
result = result and Simple is Simple
result = result and ClassAlias is Simple
result = result and ClassAlias() is not Simple()

class Rebound:
    pass

OldRebound = Rebound
old_instance = OldRebound()

class Rebound:
    pass

new_instance = Rebound()

result = result and OldRebound is not Rebound
result = result and OldRebound != Rebound
result = result and isinstance(old_instance, OldRebound)
result = result and not isinstance(old_instance, Rebound)
result = result and isinstance(new_instance, Rebound)
result = result and not isinstance(new_instance, OldRebound)

arg_error = False
try:
    Simple(1)
except TypeError:
    arg_error = True
result = result and arg_error

assert result
result
