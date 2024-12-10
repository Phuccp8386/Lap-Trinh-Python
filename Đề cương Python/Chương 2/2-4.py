# Giải và biện luận phương trình ax2 + bx + c = 0 (a != 0)
import math
a,b,c = map(int,input().split())
if a == 0:
    if b == 0 and c == 0:
        print("VSN")
    elif b == 0 and c != 0:
        print("VN")
    elif b != 0 and c == 0:
        print("x = 0")
    else:
        print("x = {:.2f}".format(-c/b))
elif b == 0:
    if c > 0:
        print("VN")
    else:
        print("x1 = -{:.2f}, x2 = {:.2f}".format(math.sqrt(-c/a),math.sqrt(-c/a)))