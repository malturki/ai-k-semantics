pos = [0, 1, 2, 3, 4, 5]
pos[1::2] = [10, 30, 50]

neg = [0, 1, 2, 3, 4, 5]
neg[4:0:-2] = (40, 20)

resized = [1, 2, 3]
resized[::1] = [7]

delpos = [0, 1, 2, 3, 4, 5, 6]
del delpos[1::2]

delneg = [0, 1, 2, 3, 4, 5]
del delneg[5:0:-2]

empty = []
empty[::1] = [1, 2]

nochange = [1, 2]
nochange[5:5:2] = ()
del nochange[5:5:2]

result = (
    pos == [0, 10, 2, 30, 4, 50]
    and neg == [0, 1, 20, 3, 40, 5]
    and resized == [7]
    and delpos == [0, 2, 4, 6]
    and delneg == [0, 2, 4]
    and empty == [1, 2]
    and nochange == [1, 2]
)
assert result
result
