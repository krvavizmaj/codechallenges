n = int(input())
a = [int(x) for x in input().rstrip().split()]
a = a*2

r = 0
i = 0
while i < len(a):
    while i < len(a) and a[i] == 0:
        i += 1
    s = 0
    while i < len(a) and a[i] == 1:
        s += 1
        i += 1
    if s > r:
        r = s

print(r)