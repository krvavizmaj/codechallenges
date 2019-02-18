def longestPalindromeSubsequence(input):
    s = input.replace(" ", "")

    a = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)): 
        a[i][i] = 1
    for i in range(0, len(s) - 1): 
        if s[i] == s[i+1]:
            a[i][i + 1] = 2
        else:
            a[i][i + 1] = 1

    for i in reversed(range(len(s) - 1)):
        for j in range(i + 2, len(s)):
            if s[i] == s[j]:
                a[i][j] = 2 + a[i + 1][j - 1]
            else:
                a[i][j] = max(a[i+1][j], a[i][j - 1])
        
    r = ""
    m = ""
    i = 0
    j = len(s) - 1
    while i != -1 and j > i:
        while j > 1 and a[i][j] == a[i][j-1]:
            j -= 1
        if j > i:
            r += s[j]
            i = s.find(s[j], i, j)
            if i >= 0:
                i += 1
            j -= 1

    if j == i:
        m = s[i]

    # for i in a:
    #     print(i)

    return  r + m + r[::-1] if i > 0 else s[0]

# s = "ABCCBDDCE"
# s = "STAR DESTROYER"
# s = "ABZYCXCBDDCE"
# s = "ONLY ELEVEN CHARACTERS REMAIN"
s = "SOMETHING"
# s = "GO ONWARD"
print(longestPalindromeSubsequence(s))