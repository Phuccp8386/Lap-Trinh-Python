import math
a=float(input())
b=float(input())
c=float(input())
if((a+b)>c and (b+c)>a and (a+c)>b):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("La tam giac")
    print("Chu vi={0}".format(2*p))
    print("Dien tich={0}".format(s))
else:
    print("Khong phai tam giac")