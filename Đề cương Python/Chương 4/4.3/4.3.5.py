n, m = map(int, input().split())
a = []
b = []
s = 0
d = 0
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(n):
    for j in range(m):
        b.append(a[i][j])
for i in b:
    d += 1 
    s += i
tb = s/d
print("{:.2f}".format(tb))
for i in range(n):
    for j in range(m):
        if a[i][j] > tb:
            print("{0} {1} {2}".format(a[i][j], i+1, j+1))
