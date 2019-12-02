import math

class SegmentTreeLeaf:
    value = 0
    flipped = False
    rangeFrom = 0
    rangeTo = 0
    left = None
    right = None
    
    def __init__(self, value, rangeFrom, rangeTo):
        self.value = value
        self.rangeFrom = rangeFrom
        self.rangeTo = rangeTo

class SegmentTree:
    __tree = None

    def __init__(self, n):
        self.__tree = self.__initTree(self.__tree, 0, n)

    def __initTree(self, root, left, right):
        root = SegmentTreeLeaf(0, left, right)

        if right > left:
            root.left = self.__initTree(root.left, left, (right + left) // 2, )
            root.right = self.__initTree(root.left, (right + left) // 2 + 1, right)

        return root

    def __getSumRecursive(self, root, rangeFrom, rangeTo):
        if root.rangeFrom > rangeTo or root.rangeTo < rangeFrom:
            return 0

        if root.flipped == True:
            root.flipped = False
            root.value = (root.rangeTo - root.rangeFrom + 1) - root.value
            if root.left != None and root.right != None:
                root.left.flipped = not root.left.flipped
                root.right.flipped = not root.right.flipped

        if rangeFrom <= root.rangeFrom and rangeTo >= root.rangeTo:
            return root.value
        else:
            return self.__getSumRecursive(root.left, rangeFrom, rangeTo) + self.__getSumRecursive(root.right, rangeFrom, rangeTo)

    def getSum(self, rangeFrom, rangeTo):
        return self.__getSumRecursive(self.__tree, rangeFrom, rangeTo)

    def __updateValuesRecursive(self, root, rangeFrom, rangeTo):
        if root.flipped == True:
            root.flipped = False
            root.value = (root.rangeTo - root.rangeFrom + 1) - root.value
            if root.left != None and root.right != None:
                root.left.flipped = not root.left.flipped
                root.right.flipped = not root.right.flipped

        if rangeFrom <= root.rangeFrom and rangeTo >= root.rangeTo:
            root.value = (root.rangeTo - root.rangeFrom + 1) - root.value

            # mark children as fliped
            if root.left != None and root.right != None:
                root.left.flipped = not root.left.flipped
                root.right.flipped = not root.right.flipped

            return root.value
        elif root.rangeFrom > rangeTo or root.rangeTo < rangeFrom:
            return root.value
        else:
            root.value = self.__updateValuesRecursive(root.left, rangeFrom, rangeTo) + self.__updateValuesRecursive(root.right, rangeFrom, rangeTo)
            return root.value

    def updateValues(self, rangeFrom, rangeTo):
        self.__updateValuesRecursive(self.__tree, rangeFrom, rangeTo)

class SegmentTreeArray:
    __tree = []

    def __init__(self, n):
        height = math.ceil(math.log(6, 2))
        self.__tree = [1 for _ in range(0, 2**(height + 1) - 1)]

    def getSum(self, rangeFrom, rangeTo, segmentFrom, segmentTo, rootIndex):
        if segmentFrom > rangeTo or segmentTo < rangeFrom:
            return 0
        elif rangeFrom <= segmentFrom and rangeTo >= segmentTo:
            return self.__tree[rootIndex]
        else:
            middle = (segmentFrom + segmentTo) // 2
            return self.getSum(rangeFrom, rangeTo, segmentFrom, middle, rootIndex + 1) + self.getSum(rangeFrom, rangeTo, middle + 1, segmentTo, rootIndex + 2)

    def updateValues(self, rangeFrom, rangeTo):
        pass

def main():
    n = 6
    tree = SegmentTreeArray(n)
    print(tree.getSum(0, 2, 0, n-1, 0))

    # [n,q] = map(int, input().rstrip().split())
    # tree = SegmentTreeArray(n)
    # for _ in range(q):
    #     [c, s, e] = map(int, input().rstrip().split())
    #     if c == 0:
    #         tree.updateValues(s, e)
    #     else:
    #         print(tree.getSum(s, e, 0, n-1, 0))

if __name__ == "__main__": 
    main()
