def binomialCoefficient(n, k):
    if k < n - k:
        j = k
        i = n - k + 1
    else:
        j = n - k
        i = k + 1
    
    if n > 67 and j > 30:
        return -1

    nom = []
    for t in range(i, n+1):
        nom.append(t)
    denom = []
    for t in range(2, j+1):
        denom.append(t)

    d = 2
    while d <= j:
        for i1 in range(0, len(nom)):
            for j1 in range(0, len(denom)):
                if denom[j1] > 1 and nom[i1] % d == 0 and denom[j1] % d == 0:
                    nom[i1] /= d
                    denom[j1] /= d      
        d += 1


    r = 1
    MAX_LONG = 2**63
    for no in nom:
        r *= no
    for d in denom:
        r /= d

    if r < MAX_LONG:
        return int(r)
    else:
        return -1
  

print(binomialCoefficient(20, 10))