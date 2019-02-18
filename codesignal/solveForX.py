def solveForX(e):
    x = -1000
    while abs(eval (e.replace('=','-(') + ")")) > 0.0000001 :
        x = round(x+0.01, 1)
    if x - int(x) == 0:
        return int(x)
    else:
        return x
    
print(solveForX("2*x + (3*x + 22.5) = (4*x - 1.4) - 3"));