cases = int(input())

for t in range(cases):
    n = int(input())
    s = input()

    if s.find(">") == -1 or s.find("<") == -1:
        print(0)
    else:
        print(min(s.find(">"), n - s.rfind("<") - 1))
