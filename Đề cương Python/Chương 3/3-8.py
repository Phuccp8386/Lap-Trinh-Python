def check(n):
    m = []
    while (n!=0):
        m.append(int(n % 2))
        n = n//2
    m.reverse()
    print(*m)
n = int(input())
check(n)