n, p, m = map(int, input().split())

a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

b = []
for i in range(p):
    row = list(map(int, input().split()))
    b.append(row)

c = []
for i in range(n):
    row = []  
    for j in range(m):
        row.append(0)  
    c.append(row) 
for i in range(n):  
    for j in range(m): 
        for k in range(p):  
            c[i][j] += a[i][k] * b[k][j]
for i in range(n):
    print(*c[i])