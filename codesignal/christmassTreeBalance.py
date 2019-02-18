def christmasTreeBalance(tree):
    n = len(tree) + 1
    isNode = [0 for _ in range(n)]
    c = [[] for _ in range(n)]
    
    for i in range(len(tree)):
        isNode[tree[i]] = 1
        c[tree[i]].append(i+1)
        c[i+1].append(tree[i])
    
    result = 1000000
    for i in range(n):
        if isNode[i] == 1:
            d = [0 for _ in range(n)]
            min = 1000000
            max = 0

            q = []
            q.append(i)
            while len(q) > 0:
                current = q.pop()
                for j in c[current]:
                    if j != i and d[j] == 0:
                        d[j] = d[current] + 1
                        q.append(j)
            
                    if isNode[j] == 0:
                        if d[j] < min:
                            min = d[j]
                        if d[j] > max:
                            max = d[j]
        
            if max - min < result:
                result = max - min
    
    return result

a = [2, 8, 0, 1, 0, 7, 3, 3, 8]
print(christmasTreeBalance(a))
