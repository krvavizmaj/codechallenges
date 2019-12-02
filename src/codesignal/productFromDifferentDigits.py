def productFromDifferentDigits(n):
    if n > 152:
        return -1
    r = [0]
    t = 0
    for i1 in range(1, 10):
        r.append(i1)
        for i2 in range(i1 + 1, 10):
            r.append(i1 * i2)
            for i3 in range(i2 + 1, 10):
                r.append(i1 * i2 * i3)
                for i4 in range(i3 + 1, 10):
                    r.append(i1 * i2 *i3 * i4)
                    for i5 in range(i4 + 1, 10):
                        r.append(i1 * i2 *i3 * i4 * i5)
                        for i6 in range(i5 + 1, 10):
                            r.append(i1 * i2 *i3 * i4 * i5 * i6) 
                            for i7 in range(i6 + 1, 10):
                                r.append(i1 * i2 *i3 * i4 * i5 * i6 *i7)
                                for i8 in range(i7 + 1, 10):
                                    r.append(i1 * i2 *i3 * i4 * i5 * i6 * i7 * i8)
                                    for i9 in range(i8 + 1, 10):
                                        r.append(i1 * i2 *i3 * i4 * i5 * i6 * i7 * i8 * i9)

    s = set(r)
    r = list(s)
    r.sort()
    return r[n]

print(productFromDifferentDigits(3))