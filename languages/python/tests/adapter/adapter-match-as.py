first = 0
first_alias = 0
match 2:
    case 1 as wrong:
        first = 99
    case 2 as selected:
        first = 1
        first_alias = selected

second = False
second_alias = ""
match "beta":
    case "alpha" | "beta" as label:
        second = label == "beta"
        second_alias = label
    case _:
        second = False

third = 0
third_alias = 0
match 7:
    case _ as anything:
        third = 3
        third_alias = anything

fourth = 0
fourth_alias = 0
match 0:
    case False as false_alias:
        fourth = 99
        fourth_alias = false_alias
    case 0 as zero_alias:
        fourth = 4
        fourth_alias = zero_alias

result = (
    first == 1
    and first_alias == 2
    and second
    and second_alias == "beta"
    and third == 3
    and third_alias == 7
    and fourth == 4
    and fourth_alias == 0
)
assert result
result
