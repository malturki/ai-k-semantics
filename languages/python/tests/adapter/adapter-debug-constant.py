result = __debug__ and bool(__debug__)
result = result and __debug__ == True
result = result and __debug__ is True

assert result
result
