def theSmallestStringCipher(key, message):
    i = 0
    j = 0

    s = [["" for _ in range(len(message) + 1)] for _ in range(len(key) + 1)]
    for i in range(1, len(message) + 1):
        s[0][i] = s[0][i-1] + message[i-1]
    for i in range(1, len(key) + 1):
        s[i][0] = s[i-1][0] + key[i-1]

    for i in range(1, len(key) + 1):
        for j in range(1, len(message) + 1):
            s[i][j] = min(s[i][j-1] + message[j-1], s[i-1][j] + key[i-1])

    return s[len(key)][len(message)]

# key = "abcba"
# message = "abcdcba"
key = "b"
message = "baa"
# key = "cba"
# message = "abcd"
print(theSmallestStringCipher(key, message))