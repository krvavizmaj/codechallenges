def howManySundays(n, startDay):
    w = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    d = w.index(startDay)
    r = 0

    while n > 0 and d + n >= 6:
        r += 1
        n -= 7
    return r

print(howManySundays(6, "Monday"))