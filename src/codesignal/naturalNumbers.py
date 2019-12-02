def naturalNumbersListing(n):
    s = 0
    i = 1
    t = 2  
    while i <= n:
        s += i
        if i < n: s += i + 1
        i += t
        t += 1
        i += t
        t += 1

    return s

print(naturalNumbersListing(3))