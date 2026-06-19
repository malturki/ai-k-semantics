text = "abcdef"

text[::-1] == "fedcba" and text[5:1:-2] == "fd" and text[:1:-2] == "fd" and text[4::-2] == "eca" and text[-1:-5:-1] == "fedc" and text[99:-99:-3] == "fc" and len(text[::-1]) == 6
