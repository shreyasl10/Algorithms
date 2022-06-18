class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


output = []


def printSpiral(root):

    if not root:
        return

    curLevel = []
    nextLevel = []

    curLevel.append(root)

    while len(curLevel) != 0 or len(nextLevel) != 0:

        while len(curLevel) != 0:
            temp = curLevel[-1]
            curLevel.pop()
            output.append(temp.data)
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)

        while len(nextLevel) != 0:
            temp = nextLevel[-1]
            nextLevel.pop()
            output.append(temp.data)
            if temp.left:
                curLevel.append(temp.left)
            if temp.right:
                curLevel.append(temp.right)

    return output


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(6)
    root.right.left = newNode(5)
    root.right.right = newNode(4)
    print("Spiral Order traversal of",
          "binary tree is ")
    print(printSpiral(root))
