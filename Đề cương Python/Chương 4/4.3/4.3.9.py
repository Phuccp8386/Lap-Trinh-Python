n, m = map(int, input().split())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
d = 0
for i in range(n):
    s = sum(a[i])
    if s % 7 == 0:
        print(i+1)
        d = 1 
if d == 0:
    print("NO")