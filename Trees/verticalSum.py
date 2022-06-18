class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


nodeMap = {}


def SumLevel(root, level):

    if not root:
        return
    SumLevel(root.left, level-1)

    if level in nodeMap.keys():
        nodeMap[level] += root.data
    else:
        nodeMap[level] = root.data

    SumLevel(root.right, level+1)


def verticalSum(root):

    level = 0
    SumLevel(root, level-1)

    for i, v in nodeMap.items():
        print(i, v, sep=',')


if __name__ == '__main__':

    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    print(verticalSum(root))
