n = int(input())
a = []
b = []
c = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(n):
    for j in range(n):
        if i == j:
            b.append(a[i][j])
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            c.append(a[i][j])
print(sum(b))
print(sum(c))