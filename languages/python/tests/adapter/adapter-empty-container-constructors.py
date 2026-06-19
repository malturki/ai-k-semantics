empty_list = list()
empty_tuple = tuple()
empty_dict = dict()
empty_set = set()

result = len(empty_list) == 0 and not empty_list and empty_list == [] and 1 not in empty_list
result = result and len(empty_tuple) == 0 and not empty_tuple and empty_tuple == () and 1 not in empty_tuple
result = result and len(empty_dict) == 0 and not empty_dict and empty_dict == {} and "x" not in empty_dict
result = result and len(empty_set) == 0 and not empty_set and empty_set == set() and 1 not in empty_set
assert result
result
