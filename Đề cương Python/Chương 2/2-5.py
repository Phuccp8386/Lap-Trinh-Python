# Giải và biện luận hệ phương trình bậc nhất 2 ẩn
a1, b1, c1 = map(int,input().split())
a2, b2, c2 = map(int,input().split())
D = a1 * b2 - a2 * b1
if D == 0:
    if (c1 * b2 - c2 * b1) == 0:
        result = "VSN"
    else:
        result = "VN"
else:
    x = (c1 * b2 - c2 * b1) / D
    y = (a1 * c2 - a2 * c1) / D
    result = f"x = {x}, y = {y}"

print(result)