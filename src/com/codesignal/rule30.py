def rule30(n):
    d = {tuple([0, 0, 0]): 0, 
         tuple([0, 0, 1]): 1,
         tuple([0, 1, 0]): 1,
         tuple([0, 1, 1]): 1,
         tuple([1, 0, 0]): 1,
         tuple([1, 0, 1]): 0,
         tuple([1, 1, 0]): 0,
         tuple([1, 1, 1]): 0}
    line = [0, 0, 1, 0, 0]
    
    for i in range(n):
        # print(line)
        newLine = [0, 0]
        for j in range(1, len(line) - 1):
            newLine.append(int(d[tuple(line[j-1:j+2])]))
        newLine.append(0)
        newLine.append(0)
        line = newLine

    return line.count(1)

print(rule30(2000))