# Comments, blank physical lines, and joined logical lines should disappear
# before the executable statement structure reaches the semantics.

part = (
    1
    + 2
    + 3
)

other = 4 + \
    5


def choose(flag):
    if flag:
        return part + other
    return 0


choose(True) == 15
