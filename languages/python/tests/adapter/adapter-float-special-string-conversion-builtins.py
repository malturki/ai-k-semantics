pos_inf = float("inf")
neg_inf = float("-inf")
notnum = float("nan")

assert str(pos_inf) == "inf"
assert repr(neg_inf) == "-inf"
assert ascii(notnum) == "nan"

result = repr([pos_inf, neg_inf, notnum])
assert result == "[inf, -inf, nan]"

assert f"{pos_inf}:{neg_inf!r}:{notnum!a}" == "inf:-inf:nan"

result == "[inf, -inf, nan]"
