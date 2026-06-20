def stop():
    return
    99

def branch(x):
    if x:
        return
    return 7

result = stop() is None
result = result and branch(True) is None
result = result and branch(False) == 7
assert result
result
