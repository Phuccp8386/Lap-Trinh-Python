def check(n):
    m = [0]*n
    i = 2
    m[0] = 0
    m[1] = 1
    while (i < n):
        m[i] = m[i-1] + m[i-2]
        i+=1
    for i in range(n):
        print(m[i] , end = " ")
n = int(input())
check(n)