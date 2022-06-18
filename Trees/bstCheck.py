class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def bstCheck(root, l, r):
    if not root:
        return True

    if l and root.data <= l.data:
        return False
    if r and root.data >= r.data:
        return False

    return bstCheck(root.left, l, root) and bstCheck(root.right, root, r)


if __name__ == '__main__':

    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    print(bstCheck(root, None, None))
