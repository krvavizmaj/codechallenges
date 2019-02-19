import math

def primeSumOfPrimeFactors(n):
    primeSum = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                primeSum += i 
                n //= i
		
    if n > 1:
        primeSum += n

    return isPrime(primeSum)

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(primeSumOfPrimeFactors(8))