s = "\xe9\u03a9\u4e2d\U0001f600"

result = s[0] == "\xe9"
result = result and s[1] == "\u03a9"
result = result and s[2] == "\u4e2d"
result = result and s[3] == "\U0001f600"
result = result and s[-1] == "\U0001f600"
result = result and s[-4] == "\xe9"

result = result and s[:2] == "\xe9\u03a9"
result = result and s[1:3] == "\u03a9\u4e2d"
result = result and s[-3:-1] == "\u03a9\u4e2d"
result = result and s[::2] == "\xe9\u4e2d"
result = result and s[::-1] == "\U0001f600\u4e2d\u03a9\xe9"
result = result and s[3:0:-2] == "\U0001f600\u03a9"

result = result and list(s) == ["\xe9", "\u03a9", "\u4e2d", "\U0001f600"]
result = result and tuple(s) == ("\xe9", "\u03a9", "\u4e2d", "\U0001f600")

out = ""
for ch in s:
    out += ch
result = result and out == s

a, b, c, d = s
result = result and a == "\xe9" and b == "\u03a9" and c == "\u4e2d" and d == "\U0001f600"

head, *middle, tail = s
result = result and head == "\xe9"
result = result and middle == ["\u03a9", "\u4e2d"]
result = result and tail == "\U0001f600"

pair_out = ""
for left, right in ["\xe9\u03a9", "\u4e2d\U0001f600"]:
    pair_out += right + left
result = result and pair_out == "\u03a9\xe9\U0001f600\u4e2d"

result = result and min(s) == "\xe9"
result = result and max(s) == "\U0001f600"

index_error = False
try:
    s[4]
except IndexError:
    index_error = True
result = result and index_error

assert result
result
