x = [int(i) for i in input().rstrip().split()]

c = x[1] + x[2] - x[3]
a = x[1] - c
b = x[2] - c
#if a >= 0 and b >= 0 and c >= 0:
print(str(a) + " " + str(b) + " " + str(c))
#else:
a = x[1] + x[0] - x[3]
c = x[1] - a
b = x[0] - a
#if a >= 0 and b >= 0 and c >= 0:
print(str(a) + " " + str(b) + " " + str(c))
#    else:
b = x[2] + x[0] - x[3]
c = x[2] - b
a = x[0] - b
#if a >= 0 and b >= 0 and c >= 0:
print(str(a) + " " + str(b) + " " + str(c))