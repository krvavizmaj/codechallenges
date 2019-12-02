def commonCharacterCount(s1, s2):
    res = 0
    if s1 > s2:
        t = s1
        s1 = s2
        s2 = t
    for i in range(len(s2)):
        try:
            if s1.index(s2[i]) != -1:
                res += 1
                s1 = s1.replace(s2[i], " ", 1)
        except ValueError:
            pass
            
    return res

print(commonCharacterCount("aabcc", "adcaa"))