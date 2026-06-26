s = "\xe9\u03a9\u4e2d\U0001f600"
two = "\xe9\u03a9"
plane1 = chr(0x10000)

result = len(s) == 4
result = result and len(two) == 2
result = result and len(plane1) == 1
result = result and len(chr(255)) == 1

result = result and format(two, "5") == "\xe9\u03a9   "
result = result and format(two, ">5") == "   \xe9\u03a9"
result = result and format(two, "^5") == " \xe9\u03a9  "
result = result and format(two, ".1") == "\xe9"
result = result and format(two, ".2s") == "\xe9\u03a9"
result = result and format(s, "6.3") == "\xe9\u03a9\u4e2d   "
result = result and f"{two:>5}:{s:.3s}" == "   \xe9\u03a9:\xe9\u03a9\u4e2d"

result = result and format(8364, "5c") == "    \u20ac"
result = result and format(0x10000, "*<3c") == "\U00010000**"

assert result
result
