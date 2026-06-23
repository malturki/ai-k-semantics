a = "old"
b = "old"
flat_too_few = False
try:
    a, b = [1]
except ValueError:
    flat_too_few = a == "old" and b == "old"

c = "old"
d = "old"
flat_too_many = False
try:
    c, d = "abc"
except ValueError:
    flat_too_many = c == "old" and d == "old"

e = "old"
f = "old"
dict_too_few = False
try:
    e, f = {"x": 1}
except ValueError:
    dict_too_few = e == "old" and f == "old"

g = "old"
h = "old"
range_too_many = False
try:
    g, h = range(3)
except ValueError:
    range_too_many = g == "old" and h == "old"

p = "old"
rest = "old"
q = "old"
star_too_few = False
try:
    p, *rest, q = []
except ValueError:
    star_too_few = p == "old" and rest == "old" and q == "old"

n1 = "old"
n2 = "old"
n3 = "old"
nested_top_too_few = False
try:
    (n1, n2), n3 = [(1, 2)]
except ValueError:
    nested_top_too_few = n1 == "old" and n2 == "old" and n3 == "old"

m1 = "old"
m2 = "old"
m3 = "old"
nested_top_too_many = False
try:
    (m1, m2), m3 = [(1, 2), 3, 4]
except ValueError:
    nested_top_too_many = m1 == "old" and m2 == "old" and m3 == "old"

result = (
    flat_too_few
    and flat_too_many
    and dict_too_few
    and range_too_many
    and star_too_few
    and nested_top_too_few
    and nested_top_too_many
)
assert result
result
