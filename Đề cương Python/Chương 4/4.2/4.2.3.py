s = input().strip()
a = input()
s = list(s)
for i in range(len(s)):
    if(s[i] == a):
        s[i] = ""
print("".join(s))