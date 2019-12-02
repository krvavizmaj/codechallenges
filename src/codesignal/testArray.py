def solution(A):
    A.sort()
    i = 0
    while i < len(A) and A[i] == i+1:
        i += 1
        
    return i+1

a = [1, 2]
print(solution(a))