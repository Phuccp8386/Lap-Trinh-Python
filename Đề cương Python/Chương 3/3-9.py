def check(n):
    m = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    s = []

    if n == 0:
        print(0)
        return
    
    while n>0:
        x = int(n % 16)
        s.append(m[x])
        n = n//16

    for i in reversed(s):
        print(i,end = "")

n = int(input())
check(n)
