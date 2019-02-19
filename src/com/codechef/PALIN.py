import math
s = input()
r = ""

n = len(s)
c = 0
for i in reversed(range(math.ceil(n / 2), n)):
    t = int(s[i]) + c
    c = 0 
    if t > int(s[n - i - 1]):
        c = 1
    r = s[n - i - 1] + r

print(r)
