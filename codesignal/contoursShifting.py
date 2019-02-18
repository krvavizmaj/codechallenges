def contoursShifting(matrix):
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    n = len(matrix)
    m = len(matrix[0])
    res = [[0 for _ in range(m)] for _ in range(n)]

    for ring in range((min(n, m) + 1) // 2):
        order = []

        ringHeight = n - ring
        ringWidth = m - ring
        i = ring
        j = ring
        if ringHeight - ring > 1 and ringWidth - ring > 1:
            for d in direction:
                while i + d[0] >= ring and i + d[0] < ringHeight and j + d[1] >= ring and j + d[1] < ringWidth:
                    order.append([i, j])
                    i += d[0]
                    j += d[1]
        else:
            if ringWidth > ringHeight:
                d = direction[0]
            else:
                d = direction[1]
            while i + d[0] >= ring and i + d[0] < ringHeight and j + d[1] >= ring and j + d[1] < ringWidth:
                order.append([i, j])
                i += d[0]
                j += d[1]
            order.append([i, j])    
        order.append([ring, ring])

        if ring % 2 == 0:
            for i in range(1, len(order)):
                res[order[i][0]][order[i][1]] = matrix[order[i-1][0]][order[i-1][1]]
        else:
            for i in range(1, len(order)):
                res[order[i-1][0]][order[i-1][1]] = matrix[order[i][0]][order[i][1]]
    return res

a = [[ 1,  2,  3,  4],
     [ 5,  6,  7,  8],
     [ 9, 10, 11, 12],
     [13, 14, 15, 16],
     [17, 18, 19, 20]]

a1 = [[1, 2, 3, 4, 5]]

a2 = [[ 1,  2,  3,  4,  5],
      [ 6,  7,  8,  9, 10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20],
      [21, 22, 23, 24, 25]]

a3 = [[1], 
      [2], 
      [3], 
      [4], 
      [5]]

a4 = [[123]]

res = contoursShifting(a4)
for o in res:
    print(o)