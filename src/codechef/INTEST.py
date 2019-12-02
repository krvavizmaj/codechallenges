# Input test
[n, k] = map(int, input().rstrip().split())

r = 0
for i in range(n):
    t = int(input().rstrip())
    if t % k == 0:
        r  += 1
        
print(r)