def pascal(n):
    row = [1]
    newRow = []
    out = open("D:\\Users\\arsovv\\Desktop\\pascal.txt", "w")
    out.write(str(row) + "\n")

    for i in range(2, n):
        for j in range(0, i):
            if j == 0:
                newRow.append(1)
            elif j == i - 1:
                newRow.append(1)
            else:
                newRow.append(row[j -1] + row[j])

        out.write(str(newRow) + "\n")
        row = newRow
        newRow = []
        i += 1

    out.close()
    return 0

pascal(1000)