from numpy import *
def differentSquares(matrix):
    a = array(matrix)
    s = []
    for i in range(0, len(a) - 1):
        for j in range(0, len(a[0]) - 1):
            s.append(tuple(map(tuple, a[i:i+2,j:j+2])))

    return len(set(s))

a = [[1, 2, 1],
     [2, 2, 2],
     [2, 2, 2],
     [1, 2, 3],
     [2, 2, 1]]

print(differentSquares(a))