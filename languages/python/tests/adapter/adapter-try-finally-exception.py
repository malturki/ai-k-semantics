first = 0
try:
    try:
        first = first + 1
        raise ValueError
    finally:
        first = first + 2
except ValueError:
    first = first + 4


def return_overrides_exception():
    try:
        raise ValueError
    finally:
        return 5


second = 0
try:
    try:
        raise ValueError
    finally:
        raise TypeError
except TypeError:
    second = 1
except ValueError:
    second = 2

third = 0
for item in range(3):
    try:
        raise ValueError
    finally:
        third = third + 1
        continue
    third = 99

fourth = 0
for item in range(3):
    try:
        raise ValueError
    finally:
        fourth = fourth + 1
        break
    fourth = 99

result = first == 7 and return_overrides_exception() == 5 and second == 1 and third == 3 and fourth == 1
assert result
result
