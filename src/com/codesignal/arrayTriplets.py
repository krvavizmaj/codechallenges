def arrayTriplets(arr):
    res = 0
    arr.sort()
    n = len(arr)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            indexBigger = findIndexOfValue(arr, n, arr[i] + arr[j], j)
            res += indexBigger - j - 1

    return res

def findIndexOfValue(arr, n, biggerThan, afterIndex):
    start = afterIndex + 1
    end = n - 1    

    while end - start > 1:
        t = (start + end) // 2
        if arr[t] >= biggerThan:
            end = t
        else:
            start = t

    if arr[end] < biggerThan:
        return end + 1
    else: 
        return start if arr[start] >= biggerThan else end

# arr = [1, 2, 10, 5, 12, 8, 2]
arr = [88, 13, 9, 6, 88, 27, 21, 25, 75, 43, 65, 94, 27, 99, 63, 100, 73, 8]
print(arrayTriplets(arr))