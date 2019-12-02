s = 0
def nForCycle(n, low, high, c):
    global s
    if n == 0:
        s += 1
        print(c)
    else:
        for i in range(low, high+1):
            c.append(i)
            nForCycle(n - 1, i, high, c)
            c.pop()

t = input()
for i in range(int(t)):
    line = input()
    n = int(line.split(" ")[0])
    k = int(line.split(" ")[1])
    if n == k:
        print(1)
    else:
        c = [1 for _ in range(k)]
        for j in range(0, n-k):
            c1 = [1]
            for l in range(1, k):
                c1.append(c[l] + c1[l-1])
            c = c1
        print(c[k - 1])

# nForCycle(5, 1, 7, [])
# print(s)
