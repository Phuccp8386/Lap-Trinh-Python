import math
def check(n):
    tong= 0
    if n < 6 : 
        return False
    elif n ==6: 
        return True
    else:
        for i in range (1,int(math.sqrt(n))+1):
            if n % i ==0:
                tong +=i
                if i != 1 and i != n // i:
                     tong += n // i
        if tong == n:
            return True
        return False
a = int(input())
b = int(input())
for i in range(a,b):
    if (check(i)):
        print(i , end = " ")

