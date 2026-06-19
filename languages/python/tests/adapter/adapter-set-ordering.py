small = {1}
same_small = {1, 1}
large = {1, 2}
overlap = {2, 3}

small < large and small <= large and large > small and large >= small and small <= same_small and not (small < same_small) and not (small < overlap) and not (large > overlap)
