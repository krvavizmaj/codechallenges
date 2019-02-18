def minesweeper(matrix):
    d = [[-1, -1],[-1, 0],[-1, 1],[0, -1],[0, 1],[1, -1],[1, 0],[1, 1]] 
    newMatrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == True:
                for k in d:
                    if i + k[0] >= 0 and i + k[0] < len(matrix) and j + k[1] >= 0 and j + k[1] < len(matrix[0]):
                        newMatrix[i + k[0]][j + k[1]] += 1

    return newMatrix


matrix = [[True,False,False,True], 
          [False,False,True,False], 
          [True,True,False,True]]
print(minesweeper(matrix))