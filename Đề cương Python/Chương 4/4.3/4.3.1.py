n, m, k = map(int, input().split())
a = []
d = 0
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for j in range(m):
        if a[i][j] == k:
            d += 1
print(d)