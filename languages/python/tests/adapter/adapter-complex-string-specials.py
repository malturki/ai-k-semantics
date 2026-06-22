result = complex("inf") == complex(float("inf"), 0)
result = result and complex("-Infinity") == complex(-float("inf"), 0)
result = result and complex("infj") == complex(0, float("inf"))
result = result and complex("-INFJ") == complex(0, -float("inf"))
result = result and complex("1+infj") == complex(1, float("inf"))
result = result and complex("-inf+1j") == complex(-float("inf"), 1)
result = result and complex("(inf-infj)") == complex(float("inf"), -float("inf"))
assert result
result
