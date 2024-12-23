n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
d = 0
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            d = 1
            break
if d == 0:
    print("YES")
else:
    print("NO")