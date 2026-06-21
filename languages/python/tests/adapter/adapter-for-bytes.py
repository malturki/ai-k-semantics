total = 0
for value in b"Az":
    total += value

result = total == 65 + 122

empty_else = False
for value in b"":
    empty_else = False
else:
    empty_else = True

result = result and empty_else

normal_else = False
for value in b"A":
    normal_else = value == 65
else:
    normal_else = normal_else and True

result = result and normal_else

break_suppresses_else = True
for value in b"AB":
    if value == 65:
        break
else:
    break_suppresses_else = False

result = result and break_suppresses_else
result
