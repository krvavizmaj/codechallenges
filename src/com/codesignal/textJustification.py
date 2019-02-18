def textJustification(words, l):
    result = []
    end = 0
    line = []
    while end < len(words):
        c = 0   
        lineLength = 0
        while end < len(words) and c + len(words[end]) <= l:
            line.append(words[end])
            lineLength += len(words[end])
            c += len(words[end]) + 1
            end += 1

        if len(line) > 1 and end < len(words):
            emptySpaces = divmod(l - lineLength, len(line) - 1)
        else:
            emptySpaces = [1, 0]

        s = ""
        for i, word in enumerate(line):
            s += word
            if i < len(line) - 1:
                for j in range(0, emptySpaces[0]):
                    s += " "
            if i < emptySpaces[1]:
                s += " "
        
        if len(line) == 1 or end == len(words):
            for j in range(len(s), l):
                s += " "

        # print("[" + s + "]")
        result.append(s)
        line = []

    return result

words =  ["Extra", "spaces", "between", "words", "should", "be", "distributed", "as", "evenly", "as", "possible.", "If", "the", "number", "of", "spaces", "on", "a", "line", "does", "not", "divide", "evenly", "between", "words,", "the", "empty", "slots", "on", "the", "left", "will", "be", "assigned", "more", "spaces", "than", "the", "slots", "on", "the", "right."]
l = 35
print(textJustification(words, l))
