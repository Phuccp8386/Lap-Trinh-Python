n, q = map(int, input().split())
s = input()
a = []
for i in range(q):
    d = 0
    l, r ,c = input().split()
    l, r = int(l), int(r)
    for j in range(l-1, r):
        if s[j] == c:
            d += 1
    a.append(d)
for i in a:
    print(i)