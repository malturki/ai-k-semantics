x = 1
y = 2
z = 0
w = 10
q = 5
r = 0


def bump():
    global x
    x = x + 4
    return x


def set_many(delta):
    global x, y
    x = x + delta
    y = y + x
    return y


def with_default(amount=3):
    global z
    z = z + amount
    return z


def keyword_update(a, b=1):
    global w
    w = w + a + b
    return w


def nested_decl(flag):
    if flag:
        global q
    q = q + 7
    return q


def fails_after_write():
    global r
    r = 9
    raise ValueError


one = bump()
two = set_many(2)
three = with_default()
four = keyword_update(a=4, b=6)
five = keyword_update(1, b=2)
six = nested_decl(True)
failed = False
try:
    fails_after_write()
except ValueError:
    failed = True

result = (
    one == 5
    and two == 9
    and three == 3
    and four == 20
    and five == 23
    and six == 12
    and x == 7
    and y == 9
    and z == 3
    and w == 23
    and q == 12
    and failed
    and r == 9
)
assert result
result
