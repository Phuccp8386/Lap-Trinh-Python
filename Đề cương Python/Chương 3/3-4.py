def check(a,b):
    while b!=0:
        a,b = b , a% b
    return abs(a)
a = int(input())
b = int(input())
print(check(a,b))