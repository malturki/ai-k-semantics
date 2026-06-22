first = 0
match 2:
    case 1 | 2:
        first = 1
    case _:
        first = 99

second = 0
match "beta":
    case "alpha" | "beta" | "gamma":
        second = 2
    case _:
        second = 99

third = 0
match None:
    case True | None:
        third = 3
    case _:
        third = 99

fourth = 0
match 4:
    case 1 | 2:
        fourth = 99
    case 3 | 4:
        fourth = 4
    case _:
        fourth = 100

fifth = 0
match 0:
    case False | 1:
        fifth = 99
    case 0:
        fifth = 5

result = first == 1 and second == 2 and third == 3 and fourth == 4 and fifth == 5
assert result
result
