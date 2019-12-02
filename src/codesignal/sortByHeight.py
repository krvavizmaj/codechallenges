def sortByHeight(a):
    one = []
    b = []
    for i,k in enumerate(a):
        if k == -1: 
            one.append(i)
        else:
            b.append(k)

    b.sort()
    for i in one: b.insert(i, -1)
    
    return b

a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))