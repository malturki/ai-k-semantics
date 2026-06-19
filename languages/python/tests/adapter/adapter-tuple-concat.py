left = (1,)
right = (2, 3)

left + right == (1, 2, 3) and () + right == right and left + () == left and (left + right)[1] == 2 and len(left + right) == 3
