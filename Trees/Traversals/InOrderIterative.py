class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def InOrder(root):
    order = []
    ptr = root
    temp = []
    while True:
        if ptr:
            temp.append(ptr)
            ptr = ptr.left
        elif temp:
            ptr = temp.pop()
            order.append(ptr)
            ptr = ptr.right
        else:
            break
    return order


root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
a = InOrder(root)
for i in range(len(a)):
    print(a[i].data, end=' ')
