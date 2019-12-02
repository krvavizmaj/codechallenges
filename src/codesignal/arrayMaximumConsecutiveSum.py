def arrayMaxConsecutiveSum(inputArray, k):
    max = sum(inputArray[0:k])
    s = max
    for i in range(k, len(inputArray)):
        s -= inputArray[i-k]
        s += inputArray[i]
        if s > max:
            max = s

    return max

a = [2, 3, 5, 1, 6]
print(arrayMaxConsecutiveSum(a, 2))