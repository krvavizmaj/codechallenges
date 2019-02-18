def expandMinesweeper(field, clickRow, clickColumn):
    if field[clickRow][clickColumn] == 0:
        dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        n = len(field)
        m = len(field[0])
        v = [[0 for _ in range(m)] for _ in range(n)]
        v[clickRow][clickColumn] = 1

        q = [[clickRow, clickColumn]]
        while len(q) > 0:
            c = q.pop(0)
            field[c[0]][c[1]] = -2
            
            for d in dir:
                if c[0] + d[0] >= 0 and \
                    c[0] + d[0] < n and \
                    c[1] + d[1] >= 0 and \
                    c[1] + d[1] < m and \
                    field[c[0] + d[0]][c[1] + d[1]] == 0 and \
                    v[c[0] + d[0]][c[1] + d[1]] == 0:
                    q.append([c[0] + d[0], c[1] + d[1]])
                    v[c[0] + d[0]][c[1] + d[1]] = 1

    return field

field = [
    [-1,1,0,0], 
    [1,1,0,0], 
    [0,0,1,1], 
    [0,0,1,-1]
]
clickRow = 3
clickColumn = 1
print(expandMinesweeper(field, clickRow, clickColumn))
