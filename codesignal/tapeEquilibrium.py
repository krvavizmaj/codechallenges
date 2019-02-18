def solution(A):
    s1 = 0
    s2 = abs(sum(A))
    min = 100000000
    for i in range(0, len(A)-1):
        s1 += A[i]
        s2 -= A[i]
        if abs(s1 - s2) < min:
            min = abs(s1 - s2)

    return min

a = [3, 1, 2, 4, 3]
print(solution(a))