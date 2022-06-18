class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Mirror(root):
    if not root:
        return
    temp = []
    temp.append(root)
    while len(temp):
        ptr = temp.pop(0)
        ptr.left, ptr.right = ptr.right, ptr.left
        if ptr.left:
            temp.append(ptr.left)
        if ptr.right:
            temp.append(ptr.right)


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print(root.data, end=" ")
    Inorder(root.right)


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
Inorder(root)
print('\n')
Mirror(root)
Inorder(root)
