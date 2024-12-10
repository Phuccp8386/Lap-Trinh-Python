# Giải và biện luận phương trình ax2 + bx + c = 0 (a != 0)

import math
a, b, c = map(int, input().split())

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(f" x1 = {x1}, x2 = {x2}")
elif d == 0:
    x = -b / (2*a)
    print(f"x = {x}")
else:
    print("VN")

