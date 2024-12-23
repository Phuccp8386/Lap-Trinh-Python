n, m = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)    
for i in range(n):
    hangc = []
    hangd = []
    for j in range(m):
        hangc.append(a[i][j]+b[i][j])
        hangd.append(a[i][j]-b[i][j])
    c.append(hangc)
    d.append(hangd)
for i in range(n):
        print(*c[i])
for i in range(n):
        print(*d[i])