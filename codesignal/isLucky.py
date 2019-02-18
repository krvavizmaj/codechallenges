def isLucky(n):
    l = len(str(n))
    s = 0
    for i in range(l // 2):
        s += n % 10
        n //= 10
    for i in range(l // 2):
        s -= n % 10
        n //= 10
        
    return s == 0

print(isLucky(1230))