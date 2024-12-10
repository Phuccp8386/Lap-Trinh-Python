import math
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())
a=math.sqrt((x1-x2)**2+(y1-y2)**2)
b=math.sqrt((x2-x3)**2+(y2-y3)**2)
c=math.sqrt((x1-x3)**2+(y1-y3)**2)
if((a+b)>c and (b+c)>a and (a+c)>b):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("La tam giac")
    print("Chu vi={0}".format(2*p))
    print("Dien tich={0}".format(s))
else:
    print("Khong phai tam giac")