text = "abcdef"

text[::2] == "ace" and text[1:6:2] == "bdf" and text[:5:2] == "ace" and text[2::3] == "cf" and text[99:100:2] == "" and len(text[::2]) == 3
