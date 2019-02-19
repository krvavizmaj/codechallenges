out = open("C:\\Users\\krvav\\Desktop\\a.txt", "w")
s = 0
n = 23

def nForLoop(k, low, high, c):
    global s
    if k == 0:
        s += 1
        out.write(str(c) + "\n")
    else:
        for i in range(low, high):
            c.append(i)
            nForLoop(k - 1, i, high, c)
            c.pop()

nForLoop(23, 0, 7, [])
# nForLoop(2, 0, 5, [])

print(s)
out.close()