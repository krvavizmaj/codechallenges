import sys

def findRoot(n, k, currentNodeIndex, nodesMap, childSum, childCount, parent):
    if k == n:
        return parent
    for i in range(1, n+1):
        if i != currentNodeIndex and childSum[i] >= nodesMap[currentNodeIndex] and childCount[i] < 2 and parent[i] != currentNodeIndex:
            childSum[i] -= nodesMap[currentNodeIndex]
            childCount[i] += 1
            parent[currentNodeIndex] = i
            
            for j in range(1, n+1):
                if parent[j] == 0:
                    result = findRoot(n, k + 1, j, nodesMap, childSum, childCount, parent)
                    if result != None:
                        return result

            parent[currentNodeIndex] = 0
            childCount[i] -= 1
            childSum[i] += nodesMap[currentNodeIndex]

testCases = sys.stdin.readline().rstrip()
while testCases == '':
    testCases = sys.stdin.readline().rstrip()

for t in range(0, int(testCases)):
    n = int(sys.stdin.readline().rstrip())
    nodesMap = [0 for _ in range(0, n+1)]
    childSum = [0 for _ in range(0, n+1)]
    childCount = [0 for _ in range(0, n+1)]
    parent = [0 for _ in range(0, n+1)]

    for k in range(0, n):
        line = sys.stdin.readline().rstrip()
        nodesMap[k+1] = int(line.split(" ")[0])
        childSum[k+1] = int(line.split(" ")[1])

    tree = findRoot(n, 1, 1, nodesMap, childSum, childCount, parent)

    k = 1
    while tree[k] != 0:
        k += 1
    print(nodesMap[k])