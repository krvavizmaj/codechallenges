n = int(input())
a = [int(x) for x in input().rstrip().split()]

r = 0
i = 0
while i < n:
    r += 1
    max = a[i]
    while i < n and i+1 < max:
        i += 1
        if a[i] > max:
            max = a[i] 
    i += 1

print(r)