class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


output = []


def boundaryLeft(root):
    if root:
        if root.left:
            output.append(root.data)
            boundaryLeft(root.left)
        elif root.right:
            output.append(root.data)
            boundaryLeft(root.right)


def boundaryLeaves(root):
    if root:
        boundaryLeaves(root.left)

        if not root.left and not root.right:
            output.append(root.data)

        boundaryLeaves(root.right)


def boundaryRight(root):
    if root:
        if root.right:
            boundaryRight(root.right)
            output.append(root.data)
        elif root.left:
            boundaryRight(root.left)
            output.append(root.data)


def boundaryTraversal(root):
    if root:
        output.append(root.data)

    boundaryLeft(root.left)

    boundaryLeaves(root.left)
    boundaryLeaves(root.right)

    boundaryRight(root.right)


root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
boundaryTraversal(root)
print(output)
