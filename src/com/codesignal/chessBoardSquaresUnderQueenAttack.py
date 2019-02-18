def chessBoardSquaresUnderQueenAttack(a, b):
    s = (a + b - 2) * a * b
    for i in range(a):
        for j in range(b):
            s += min(i, j) + min(a-1 - i, j) + min(i, b-1 - j) + min(a-1 - i, b-1 - j)
    
    return s


print(chessBoardSquaresUnderQueenAttack(2, 3))

