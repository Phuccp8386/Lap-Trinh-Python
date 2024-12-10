import math
ep=float(input())
x=int(input())
if(ep>0 and ep<1):
    s=0
    k=0
    while(abs(math.pow(x,k)/(math.factorial(2*k+1)))<ep):
        s+=math.pow(x,k)/(math.factorial(2*k+1))
        k+=1
print(s)