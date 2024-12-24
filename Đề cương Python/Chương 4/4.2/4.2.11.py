import re
s = input()
x = re.findall(r"\d+",s)
x = list(map(int, x))
M = max(x)
print(M)