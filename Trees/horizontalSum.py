class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


output = []


def levelSum(root):

    if not root:
        return

    curLevel = []
    nextLevel = []

    curLevel.append(root)
    maxSum = 0
    while len(curLevel) != 0 or len(nextLevel) != 0:
        s = 0
        if len(curLevel) != 0:
            for i in curLevel:
                s += i.data
            maxSum = max(maxSum, s)
        while len(curLevel) != 0:
            temp = curLevel[-1]
            curLevel.pop()
            output.append(temp.data)
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)
        s = 0
        if len(nextLevel) != 0:
            for i in nextLevel:
                s += i.data
            maxSum = max(maxSum, s)

        while len(nextLevel) != 0:
            temp = nextLevel[-1]
            nextLevel.pop()
            output.append(temp.data)
            if temp.right:
                curLevel.append(temp.right)
            if temp.left:
                curLevel.append(temp.left)

    return maxSum


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(22)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(6)
    root.right.left = newNode(5)
    root.right.right = newNode(4)
    print(levelSum(root))
