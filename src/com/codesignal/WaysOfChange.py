def waysOfChange(amount):
    n = [1, 1]
    g2 = [1, 0]
    g5 = [1, 0]
    g10 = [1, 0]

    for i in range(2, amount+1):
        n.append(n[i-1] + g2[i-2])
        g2.append(0)
        g5.append(0)
        g10.append(0)

        g2[i] += g2[i-2]
        if i - 5 >= 0:
            n[i] += g5[i-5]
            g2[i] += g5[i-5]
            g5[i] += g5[i-5]
        if i - 10 >= 0:
            n[i] += g10[i-10]
            g2[i] += g10[i-10]
            g5[i] += g10[i-10]
            g10[i] += g10[i-10]

    return n[amount]

print(waysOfChange(237))