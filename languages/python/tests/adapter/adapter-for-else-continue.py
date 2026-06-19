total = 0
for i in range(3):
    if i == 2:
        continue
    total += i
else:
    total += 10

total == 11
