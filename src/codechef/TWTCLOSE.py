line = input()
n = line.split(" ")[0]
k = line.split(" ")[1]

s = []
for i in range(int(k)):
    line = input()
    p = line.split(" ")
    if p[0] ==  "CLOSEALL":
        s.clear()
    else:
        t = p[1]
        if t in s:
            s.remove(t)
        else:
            s.append(t)
    print(len(s))