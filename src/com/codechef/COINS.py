import sys

d = {0: 0, 1: 1}
def calculate(n):
    if n in d:
        return d[n]

    max = n
    splitValue = calculate(n // 2) + calculate(n // 3) + calculate(n // 4)
    if splitValue > max:
        max = splitValue

    d[n] = max
    return max
    
for n in sys.stdin:
    print(calculate(int(n)))

