class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def leftView(root):
    queue = [root]
    output = []
    while len(queue) > 0:
        n = len(queue)
        for i in range(n):
            temp = queue.pop(0)
            if i == 0:
                output.append(temp.data)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    return output


if __name__ == '__main__':

    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    print(leftView(root))
