import math

def herbGarden(plants, days):
    maximums = findMaximums(plants)

    if days == 1:
        return plants[maximums[0]] // 2
        
    maxSum = 0
    for j in maximums:
        sum = plants[j] // 2
        t = plants[j]
        plants[j] = math.ceil(plants[j] / 2)
        for k in range(len(plants)):
            plants[k] += 2

        sum += herbGarden(plants, days - 1)
        if sum > maxSum:
            maxSum = sum

        for k in range(len(plants)):
            plants[k] -= 2
        plants[j] = t

    return maxSum

def findMaximums(plants):
    res = []
    maximums = []
    max = 0
    for i,p in enumerate(plants):
        if p // 2 > max:
            max = p // 2
            res.clear()
            maximums.clear()
            res.append(i)
            maximums.append(p)
        elif p // 2 == max and not (p in maximums):
            res.append(i)
            maximums.append(p)

    return res

plants = [8, 7, 99]
days = 16
# plants = [1, 1, 1, 100]
# days = 15
# plants = [8, 9]
# days = 4
print(herbGarden(plants, days))