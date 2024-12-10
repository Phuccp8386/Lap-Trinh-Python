# Giải và biện luận phương trình ax + b = 0
a,b = map(int,input().split())
if a == 0 and b == 0:
    print("VSN")
elif a == 0 and b != 0:
    print("VN")
elif a != 0 and b ==0:
    print("VSN")
else:
    print("x = {0}".format(-b/a))