def countAtoms(molecule):
    expanded = ""

    i = 0
    while i < len(molecule):
        if molecule[i] == "[" or molecule[i] == "(" or molecule[i] == "{":
            lastBracket = findClosingBracketIndex(molecule, i)
            repeats = readNumberFromIndex(molecule, lastBracket + 1)
            repeatsAsInt = int(repeats) if repeats != "" else 1
            expanded += expandString(molecule[i + 1:-(len(molecule) - lastBracket)], repeatsAsInt)
            expanded += molecule[lastBracket + len(str(repeats)) + 1:]
            molecule = expanded
            expanded = ""
            i = 0
        else:
            expanded += molecule[i]
            i += 1

    start = 0
    result = {}
    while start < len(expanded):
        end = start + 1
        while end < len(expanded) and (expanded[end] < "A" or expanded[end] > "Z"):
            end += 1
        if end < len(expanded):
            addAtoms(expanded[start:-len(expanded) + end], result)
        else:
            addAtoms(expanded[start:], result)
        start = end

    resultKeys = list(result.keys())
    resultKeys.sort()
    out = ""
    for s in resultKeys:
        out += s
        out += str(result.get(s))

    return out

def addAtoms(part, result):
    start = 0
    while start < len(part) and (part[start] < "0" or part[start] > "9"):
        start += 1

    atom = part[0:start]
    n = 1
    if start < len(part):
        n = int(readNumberFromIndex(part, start))

    result[atom] = result.get(atom, 0) + n

def findClosingBracketIndex(inputString, startIndex):
    c = 1
    i = startIndex + 1
    closedBracket = "]" if inputString[startIndex] == "[" else ")" if inputString[startIndex] == "(" else "}"

    while c != 0:
        if inputString[i] == inputString[startIndex]:
            c += 1
        elif inputString[i] == closedBracket:
            c -= 1
        i += 1
    return i - 1

def readNumberFromIndex(inputString, startIndex):
    n = ""
    j = startIndex
    while j < len(inputString) and inputString[j] >= "0" and inputString[j] <= "9":
        n += inputString[j]
        j += 1
    return n

def expandString(inputString, n):
    s = ""
    for i in range(n):
        s += inputString
    return s

print(countAtoms("[Cu(NH3)4(H2O)2]SO4"))