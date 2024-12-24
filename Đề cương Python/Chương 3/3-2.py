import math
def check(n):
    if(n<2): return False
    elif (n==2): return True
    else:
        for i in range(2,int (math.sqrt(n))+1):
            if n % i ==0:
                return False
        return True
n = int(input())
for i in range(n):
    if check(i):
        print(i,end = " ")