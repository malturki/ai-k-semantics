#!/usr/bin/env python3
# coding: utf-8

# Leading comments and blank logical lines are part of file_input framing, not
# executable statements.

seed = 1

if seed:
    branch = 2
else:
    branch = 0

after = branch; total = after + seed

# A final expression before ENDMARKER keeps the current adapter smoke oracle
# simple while still passing through ordinary file input.
result = total == 3

result
