first = False
match "payload":
    case captured:
        first = captured == "payload"

second = 0
match 3:
    case 1:
        second = 100
    case other:
        second = other + 4

third = 0
match True:
    case True:
        third = 1
    case fallback:
        third = 99

fourth = 0
match "tail":
    case "head":
        fourth = 1
    case tail_capture:
        fourth = tail_capture == "tail"

result = first and captured == "payload" and second == 7 and other == 3 and third == 1 and fourth == True and tail_capture == "tail"
assert result
result
