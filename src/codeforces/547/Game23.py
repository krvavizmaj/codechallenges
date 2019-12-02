line = input()
n = int(line.split(" ")[0])
m = int(line.split(" ")[1])

if m % n != 0:
    print(-1)
else:
    r = 0
    d = m // n
    while d > 1 and d % 2 == 0:
        d = d // 2
        r += 1
    while d > 1 and d % 3 == 0:
        d = d // 3
        r += 1
    if d > 1:
        print(-1)
    else:
        print(r)
