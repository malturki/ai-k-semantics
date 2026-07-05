import math
import math as m
from math import pi as circle_pi
from math import tau

result = (
    math.__name__ == "math"
    and m is math
    and math.pi > 3.0
    and circle_pi == math.pi
    and tau > 6.0
)

result
