n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
d = 0
for i in range(n):
    for j in range(n):
        if i > j:
            if a[i][j] != 0:
                d = 1 
                break

e = 0
for i in range(n):
    for j in range(n):
        if i < j:
            if a[i][j] != 0:
                e = 1 
                break
if d == 0:
    print("UPPER TRIANGLE")
if e == 0:
    print("LOWER TRIANGLE")
if e ==1 and d==1:
    print("NONE")
    