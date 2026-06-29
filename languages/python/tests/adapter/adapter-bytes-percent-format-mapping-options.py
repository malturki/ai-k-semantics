fmt = b"%(x)+05d|%(y)#06x|%(z).3d|%(word)5.2b|%(long)ld"
out = fmt % {
    b"x": 7,
    b"y": 12,
    b"z": 5,
    b"word": b"abcdef",
    b"long": 9,
}

result = out == b"+0007|0x000c|005|   ab|9"

assert result
result
