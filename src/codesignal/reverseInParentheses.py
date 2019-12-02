def reverseInParentheses(inputString):
    s = inputString.find("(")
    while s != -1:
        i = s
        c = 1
        while c != 0:
            i += 1
            if inputString[i] == "(":
                c += 1
            elif inputString[i] == ")":
                c -= 1

        newString = inputString[:s] + reverseString(inputString[s+1:i]) + inputString[i+1:]
        inputString = newString
        s = inputString.find("(")

    return inputString

def reverseString(s):
    newS = ""
    for i in reversed(range(0, len(s))):
        if s[i] == "(":
            newS += ")"
        elif s[i] == ")":
            newS += "("
        else:
            newS += s[i]
    return newS

inputString = "foo(bar(baz))blim"
print(reverseInParentheses(inputString))
