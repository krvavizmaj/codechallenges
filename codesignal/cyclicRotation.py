def solution(A, K):
    k = K % len(A)
    return A[len(A) - k:] + A[0:len(A) - k]

a = [3, 8, 9, 7, 6]
k = 3
print(solution(a, k))