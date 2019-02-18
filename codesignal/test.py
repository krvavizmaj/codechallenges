def test():
    s = [0 for _ in range(10)]
    return s

def almostIncreasingSequence(sequence):
    skip = 0
    n = len(sequence)
    i = 0
    while i < n - 1:
        if sequence[i] < sequence[i+1]:
            i += 1
        else:
            if skip == 1:
                return False

            if i == 0 or i+2 >= n or sequence[i-1] < sequence[i+1] or sequence[i] < sequence[i+2]:
                skip += 1
                i += 1
            else:
                return False

                
    return True

print(almostIncreasingSequence([1, 2, 3, 4, 5, 3]))