class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diagonalBT(root):
    output = []
    if not root:
        return
    queue = [root]
    queue.append(None)

    while len(queue):
        temp = queue.pop(0)

        if not temp:
            if len(queue) == 0:
                return output
            output.append(' ')

            queue.append(None)
        else:
            while temp:
                output.append(temp.data)

                if temp.left:
                    queue.append(temp.left)

                temp = temp.right


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = node1 = newNode(3)
    root.left.left = node2 = newNode(7)
    root.left.right = newNode(6)
    root.right.left = newNode(5)
    root.right.right = newNode(4)
    print(diagonalBT(root))
