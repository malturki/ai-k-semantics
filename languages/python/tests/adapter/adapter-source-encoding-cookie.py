#!/usr/bin/env python3
# coding: latin-1

text = "café"

result = (
    text == "caf\u00c3\u00a9"
    and len(text) == 5
    and text[-2] == "\u00c3"
    and text[-1] == "\u00a9"
)

result
