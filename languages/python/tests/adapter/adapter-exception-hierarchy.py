arith = False
try:
    1 // 0
except ArithmeticError:
    arith = True

lookup_index = False
try:
    [][0]
except LookupError:
    lookup_index = True

lookup_key = False
try:
    {}["missing"]
except (ArithmeticError, LookupError):
    lookup_key = True

base = False
try:
    raise TypeError
except BaseException:
    base = True

instance_base = False
try:
    raise ValueError(1, 2)
except Exception as err:
    instance_base = True

ordered = 0
try:
    raise RuntimeError
except LookupError:
    ordered = 10
except Exception:
    ordered = 2

specific_first = 0
try:
    raise KeyError
except LookupError:
    specific_first = 1
except KeyError:
    specific_first = 10

result = (
    arith
    and lookup_index
    and lookup_key
    and base
    and instance_base
    and ordered == 2
    and specific_first == 1
)
assert result
result
