((dk1, dk2),) = [{"left": 1, "right": 2}]
result = dk1 == "left" and dk2 == "right"

((sa, sb),) = [{1, 2}]
result = result and {sa, sb} == {1, 2}

assert result
result
