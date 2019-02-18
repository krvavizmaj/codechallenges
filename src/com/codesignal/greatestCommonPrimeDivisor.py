def greatestCommonPrimeDivisor(a, b):
    for i in reversed(range(2, min(a, b))):
        if a % i == 0 and b % i == 0 and isPrime(i):
            return i
    return -1

def isPrime(n):
    i = 2
    while i*i < n:
        if n % i == 0:
            return False
        i += 1
    return True

print(greatestCommonPrimeDivisor(100, 140))