def changeRoot(parent, newRoot):
    newParent = parent.copy()

    newParent[newRoot] = newRoot
    root = newRoot
    while parent[root] != root:
        root = parent[root]
        newParent[root] = newRoot
        newRoot = root

    return newParent

parent = [0, 0, 0, 1, 1, 1, 2, 2, 7]
newRoot = 7
print(changeRoot(parent, newRoot))