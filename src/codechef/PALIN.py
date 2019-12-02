import sys

# s = input()
s = sys.stdin.buffer.read()

n = len(s)
first = s[:n // 2]
last = ""
middle = ""
if n % 2 == 0:
    last = s[n // 2:]
else:
    last = s[n // 2 + 1:] 
    middle = s[n // 2]

if (int(first[::-1]) > int(last)):
    print(first + middle + first[::-1])

# print(first)
# print(last)
# print(middle)