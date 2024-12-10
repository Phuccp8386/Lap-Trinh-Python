# Giải và biện luận bất phương trình ax + b > 0
a,b = map(int,input().split())
if a == 0 and b>0:
    print("VSN")
elif a == 0 and b <=0:
    print("VN")
elif a > 0 and b == 0:
    print("x > 0")
elif a < 0 and b == 0:
    print("x < 0")
else:
    if -b/a > 0:
        print("x > {:.2f}".format(-b/a))
    else:
        print("x < {:.2f}".format(-b/a))