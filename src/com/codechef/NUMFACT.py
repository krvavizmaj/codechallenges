import math
import sys

cases = int(sys.stdin.readline().rstrip())

for t in range(cases):
        n = int(sys.stdin.readline().rstrip())
        a = [int(x) for x in sys.stdin.readline().rstrip().split()]
        p = []
        for num in a:
                k = num
                for i in range(2, math.ceil(math.sqrt(k)) + 1):
                        while k % i == 0:
                                p.append(i)
                                k /= i
                if k > 1:
                        p.append(k)

        res = 1
        for i in set(p):
                res *= p.count(i) + 1

        print(res)      