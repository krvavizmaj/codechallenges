def periodicSequence(s0, a, b, m):
    s = [s0]
    for i in range(1, 100):
        s.append((a * s[i - 1] + b) % m)

    for i in range(1, 100):
        period = True
        for j in range(1, i+1):
            if s[100 - j] != s[100 - j - i]:
                period = False
                break
        
        if period == True:
            return i

    return -1

print(periodicSequence(11, 2, 6, 12))
