total = 0
for x in [1, 2, 3, 4]:
    if x == 3:
        continue
    if x == 4:
        break
    total += x

total == 3
