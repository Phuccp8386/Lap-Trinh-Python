n = int(input())
for i in range(1, n + 1):
    s = input()
    ktt = s[0]
    C = 1
    kq = ""
    for j in range(1,len(s)):
        if s[j] == ktt:
            C = C + 1
        else:
            kq = kq + "{0}{1}".format(ktt,C)
            ktt = s[j]
            C = 1
    kq = kq + "{0}{1}".format(ktt,C)
    print(kq)
