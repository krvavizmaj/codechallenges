def solution(A):
    A.sort()
    i = 0
    
    while i < len(A):
        s = 1
        while i < len(A)-1 and A[i + 1] == A[i]:
            i += 1
            s += 1

        if s % 2 == 1:
            return A[i]
        
        i += 1

    return A[len(A) - 1]

a = [9, 3, 9, 3, 9, 10, 9]
print(solution(a))