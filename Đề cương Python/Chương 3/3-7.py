def check(n):
    tong = 0
    while n!=0:
        x = int(n%10)
        n = int(n/10)
        tong += x
    return tong
n = int(input())
print(check(n))
