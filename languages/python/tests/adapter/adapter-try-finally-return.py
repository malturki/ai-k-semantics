def preserve_return():
    try:
        return 1
    finally:
        pass


def override_return():
    try:
        return 1
    finally:
        return 2


def branch_return(flag):
    try:
        if flag:
            return 3
        return 4
    finally:
        pass


result = preserve_return() == 1
result = result and override_return() == 2
result = result and branch_return(True) == 3
result = result and branch_return(False) == 4
assert result
result
