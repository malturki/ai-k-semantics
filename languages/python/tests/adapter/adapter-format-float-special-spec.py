pos = float("inf")
neg = float("-inf")
nan = float("nan")

result = format(pos, "e") == "inf"
result = result and format(pos, "E") == "INF"
result = result and format(pos, "f") == "inf"
result = result and format(pos, "F") == "INF"
result = result and format(pos, "g") == "inf"
result = result and format(pos, "G") == "INF"
result = result and format(pos, "n") == "inf"
result = result and format(pos, "%") == "inf%"

result = result and format(neg, "e") == "-inf"
result = result and format(neg, "G") == "-INF"
result = result and format(neg, "%") == "-inf%"

result = result and format(nan, "e") == "nan"
result = result and format(nan, "F") == "NAN"
result = result and format(nan, "%") == "nan%"

result = result and format(pos, "+e") == "+inf"
result = result and format(nan, " e") == " nan"
result = result and format(neg, "+F") == "-INF"

result = result and format(pos, "8e") == "     inf"
result = result and format(neg, ">8e") == "    -inf"
result = result and format(pos, "<8e") == "inf     "
result = result and format(nan, "^8e") == "  nan   "
result = result and format(neg, "=8e") == "-    inf"
result = result and format(neg, "*=8e") == "-****inf"

result = result and format(pos, "08e") == "00000inf"
result = result and format(neg, "+08e") == "-0000inf"
result = result and format(nan, "+08e") == "+0000nan"

result = result and format(pos, "#.2e") == "inf"
result = result and format(pos, "z.2f") == "inf"
result = result and format(neg, "8n") == "    -inf"
result = result and format(pos, "+08") == "+0000inf"
result = result and format(neg, "08%") == "-000inf%"

assert result
result
