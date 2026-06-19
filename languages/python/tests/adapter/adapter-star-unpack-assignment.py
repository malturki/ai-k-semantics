a, *middle, z = [1, 2, 3, 4]
result = a == 1 and middle == [2, 3] and z == 4
*prefix, last = (5, 6, 7)
result = result and prefix == [5, 6] and last == 7
first, *tail = (8, 9)
result = result and first == 8 and tail == [9]
only, *empty_tail = [10]
result = result and only == 10 and empty_tail == []
*all_items, = [11, 12]
result = result and all_items == [11, 12]
*empty_only, = []
result = result and empty_only == []
same, *same = [1, 2, 3]
result = result and same == [2, 3]
*again, again = [4, 5, 6]
result = result and again == 6
assert result
result
