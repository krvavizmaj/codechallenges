def avoidObstacles(inputArray):
    o = [0 for _ in range(max(inputArray) + 1)]
    for i in inputArray:
        o[i] = 1

    for step in range(1, len(o)):
        i = 0
        while i < len(o) and o[i] == 0:
            i += step 
        if i >= len(o):
            return step

    return len(o)

a = [19, 32, 11, 23]
print(avoidObstacles(a))
