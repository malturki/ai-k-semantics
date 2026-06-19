empty = []
prefix = [1]
left = [1, 2]
same_left = [1, 2]
right = [1, 3]
longer = [1, 2, 0]

empty < prefix and prefix < left < right and left <= same_left and left >= same_left and left < longer and not (right < left) and not (longer < left)
