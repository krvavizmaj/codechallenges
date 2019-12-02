def isSkewSymmetricMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(0, i+1):
            if matrix[i][j] != -(matrix[j][i]):
                return False
            
    return True

a = [[0]]
print(isSkewSymmetricMatrix(a))