def findRoot(n, k, currentNode, childSum, childCount, parent):
    if k == n:
        return parent
    for i in range(1, n+1):
        if i != currentNode and childSum[i] >= currentNode and childCount[i] < 2 and parent[i] != currentNode:
            childSum[i] -= currentNode
            childCount[i] += 1
            parent[currentNode] = i
            
            for j in range(1, n+1):
                if parent[j] == 0:
                    return findRoot(n, k + 1, j, childSum, childCount, parent)

            parent[currentNode] = 0
            childCount[i] -= 1
            childSum[i] += currentNode

testCases = input()
for t in range(0, int(testCases)):
    n = int(input())
    nodeMap = [0 for _ in range(0, n+1)]
    childSum = [0 for _ in range(0, n+1)]
    childCount = [0 for _ in range(0, n+1)]
    parent = [0 for _ in range(0, n+1)]

    for k in range(0, n):
        line = input()
        nodeMap[k+1] = int(line.split(" ")[0])
        childSum[k+1] = int(line.split(" ")[1])
    tree = findRoot(n, 1, 1, childSum, childCount, parent)

    k = 1
    while tree[k] != 0:
        k += 1
    print(nodeMap[k])