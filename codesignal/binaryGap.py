def solution(N):
    max = 0
    while N % 2 == 0:
        N = N // 2

    while N > 0:
        while N > 0 and N % 2 == 1:
            N = N // 2
        if N > 0:
            r = 0
            while N % 2 == 0:
                N = N // 2
                r += 1
            if r > max:
                max = r
    
    return max

print(solution(2146483621))