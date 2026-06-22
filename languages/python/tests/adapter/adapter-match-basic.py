first = 0
match 2:
    case 1:
        first = 1
    case 2:
        first = 2
    case _:
        first = 3

second = 0
match 9:
    case 1:
        second = 1
    case 2:
        second = 2
    case _:
        second = 3

third = 0
match 1:
    case True:
        third = 99
    case 1:
        third = 1
    case _:
        third = 2

fourth = 0
match 0:
    case False:
        fourth = 99
    case 0:
        fourth = 1
    case _:
        fourth = 2

fifth = 0
match None:
    case None:
        fifth = 1
    case _:
        fifth = 99

sixth = 0
match "alpha":
    case "beta":
        sixth = 1
    case "alpha":
        sixth = 2
    case _:
        sixth = 3

seen = 0
seventh = 0
match (seen := seen + 1):
    case 1:
        seventh = 1
    case _:
        seventh = 2

result = first == 2 and second == 3 and third == 1 and fourth == 1 and fifth == 1 and sixth == 2 and seen == 1 and seventh == 1
assert result
result
