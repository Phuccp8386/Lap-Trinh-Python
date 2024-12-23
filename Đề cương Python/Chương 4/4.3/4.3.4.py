n, m = map(int, input().split())
a = []
b = []
c = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)    
for i in range(n):
    hangc = []
    for j in range(m):
        hangc.append(a[i][j]+b[i][j])
    c.append(hangc)
for i in range(n):
        print(*c[i])