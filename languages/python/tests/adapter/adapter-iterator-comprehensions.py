result = True

numbers = iter([0, 1, 2, 3, 4])
result = result and [n * 10 for n in numbers if n % 2 == 0] == [0, 20, 40]
result = result and next(numbers, 99) == 99

empty_list_it = iter([])
result = result and [n for n in empty_list_it] == []
result = result and next(empty_list_it, 100) == 100

filtered = iter([0, 1, 2, 3, 4])
result = result and [n for n in filtered if n > 0 if n < 4] == [1, 2, 3]
result = result and next(filtered, 101) == 101

pairs = iter([[1, 2], [3, 4]])
result = result and [a + b for a, b in pairs] == [3, 7]
result = result and next(pairs, 102) == 102

set_items = iter([1, 2, 2, 3, 4])
result = result and {n % 3 for n in set_items if n > 1} == {0, 1, 2}
result = result and next(set_items, 103) == 103

set_pairs = iter([[1, 2], [3, 4]])
result = result and {a + b for a, b in set_pairs} == {3, 7}
result = result and next(set_pairs, 104) == 104

dict_items = iter([1, 2, 3, 4])
result = result and {n: n * n for n in dict_items if n != 2} == {1: 1, 3: 9, 4: 16}
result = result and next(dict_items, 105) == 105

dict_pairs = iter([[1, 2], [3, 4], [5, 6]])
result = result and {a: b for a, b in dict_pairs if a < 5} == {1: 2, 3: 4}
result = result and next(dict_pairs, 106) == 106

source = iter([5, 6, 9])


def pull():
    return next(source)


callable_items = iter(pull, 9)
result = result and [n + 1 for n in callable_items] == [6, 7]
result = result and next(callable_items, 107) == 107

assert result
result
