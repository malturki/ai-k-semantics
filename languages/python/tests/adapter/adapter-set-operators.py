left = {1, 2, 3}
right = {3, 4}

union_ok = (
    (left | right) == {1, 2, 3, 4}
    and left == {1, 2, 3}
    and right == {3, 4}
)

intersection_ok = ({1, 2, 3} & {2, 3, 4}) == {2, 3}
difference_ok = ({1, 2, 3, 4} - {2, 4}) == {1, 3}
symmetric_difference_ok = ({1, 2, 3} ^ {2, 4}) == {1, 3, 4}

empty_ok = (
    (set() | {1}) == {1}
    and ({1} | set()) == {1}
    and (set() & {1}) == set()
    and ({1} & set()) == set()
    and (set() - {1}) == set()
    and ({1} - set()) == {1}
    and (set() ^ {1}) == {1}
    and ({1} ^ set()) == {1}
)

union_target = {1, 2}
union_target |= {2, 3}
inplace_union_ok = union_target == {1, 2, 3}

intersection_target = {1, 2, 3}
intersection_target &= {2, 3, 4}
inplace_intersection_ok = intersection_target == {2, 3}

difference_target = {1, 2, 3, 4}
difference_target -= {2, 4}
inplace_difference_ok = difference_target == {1, 3}

symmetric_difference_target = {1, 2, 3}
symmetric_difference_target ^= {2, 4}
inplace_symmetric_difference_ok = symmetric_difference_target == {1, 3, 4}

int_regression = 12
int_regression &= 10
int_regression ^= 6
int_regression |= 1
int_augmented_ok = int_regression == 15

errors_ok = True

try:
    {1} | [2]
except TypeError:
    pass
else:
    errors_ok = False

try:
    [1] | {2}
except TypeError:
    pass
else:
    errors_ok = False

try:
    {1} & [1]
except TypeError:
    pass
else:
    errors_ok = False

try:
    [1] & {1}
except TypeError:
    pass
else:
    errors_ok = False

try:
    {1} - [1]
except TypeError:
    pass
else:
    errors_ok = False

try:
    [1] - {1}
except TypeError:
    pass
else:
    errors_ok = False

try:
    {1} ^ [1]
except TypeError:
    pass
else:
    errors_ok = False

try:
    [1] ^ {1}
except TypeError:
    pass
else:
    errors_ok = False

bad_inplace = {1}
try:
    bad_inplace |= [2]
except TypeError:
    pass
else:
    errors_ok = False

result = (
    union_ok
    and intersection_ok
    and difference_ok
    and symmetric_difference_ok
    and empty_ok
    and inplace_union_ok
    and inplace_intersection_ok
    and inplace_difference_ok
    and inplace_symmetric_difference_ok
    and int_augmented_ok
    and errors_ok
)
assert result
result
