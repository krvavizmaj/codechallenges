def slalomSkiing(flags, threshold):
    start = [-1, 1]
    result = -1

    for i in range(0, 2):
        dir = start[i]
        flag = 0
        pos = flags[flag]
        while flag < len(flags) and abs(flags[flag] + dir - pos) <= threshold:
            pos = flags[flag] + dir
            flag += 1
            dir *= -1
        if flag > result: 
            result = flag

    return -1 if result == len(flags) else result

print(slalomSkiing([4,3,8,10], 4))