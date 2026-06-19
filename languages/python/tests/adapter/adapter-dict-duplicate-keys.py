d = {"x": 1, "x": 2, "y": 3}
e = {1: "int", True: "bool"}

d["x"] == 2 and len(d) == 2 and d["y"] == 3 and e[1] == "bool" and len(e) == 1 and True in e
