def zero():
    return 0


def one(x):
    return x


def two(x, y):
    return x + y


zero_lambda = lambda: 0
one_lambda = lambda x: x
two_lambda = lambda x, y: x + y

zero_extra = False
try:
    zero(1)
except TypeError:
    zero_extra = True

one_missing = False
try:
    one()
except TypeError:
    one_missing = True

one_extra = False
try:
    one(1, 2)
except TypeError:
    one_extra = True

two_missing = False
try:
    two(1)
except TypeError:
    two_missing = True

lambda_zero_extra = False
try:
    zero_lambda(1)
except TypeError:
    lambda_zero_extra = True

lambda_one_missing = False
try:
    one_lambda()
except TypeError:
    lambda_one_missing = True

lambda_one_extra = False
try:
    one_lambda(1, 2)
except TypeError:
    lambda_one_extra = True

lambda_two_missing = False
try:
    two_lambda(1)
except TypeError:
    lambda_two_missing = True

result = (
    zero() == 0
    and one(3) == 3
    and two(2, 4) == 6
    and zero_lambda() == 0
    and one_lambda(5) == 5
    and two_lambda(1, 2) == 3
    and zero_extra
    and one_missing
    and one_extra
    and two_missing
    and lambda_zero_extra
    and lambda_one_missing
    and lambda_one_extra
    and lambda_two_missing
)
assert result
result
