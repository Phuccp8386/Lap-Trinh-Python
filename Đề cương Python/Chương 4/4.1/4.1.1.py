n, k = map(int, input().split())
a = set(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(k):
    if b[i] in a:
        print("YES")
    else:
        print("NO")
    
        