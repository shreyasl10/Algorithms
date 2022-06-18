class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def SearchBT(root, key):
    if not root:
        return
    if root.left and root.left.data == key:
        return root
    if root.right and root.right.data == key:
        return root

    l = SearchBT(root.left, key)
    if l:
        return l
    r = SearchBT(root.right, key)
    return r


def btSwap(root, node1, node2):
    if not root:
        return
    left1 = None
    left2 = None
    right1 = None
    right2 = None

    # Store parent of first node
    parent1 = SearchBT(root, node1.data)

    # Store left & Right children of first node
    if node1 and node1.left:
        left1 = node1.left
    if node1 and node1.right:
        right1 = node1.right

    # Store parent of second node
    parent2 = SearchBT(root, node2.data)
    # Store left & Right children of first node
    if node2 and node2.left:
        left2 = node2.left
    if node2 and node2.right:
        right2 = node2.right

    # Swapping first node's parent link to node2
    if parent1.left and parent1.left == node1:
        parent1.left = node2
    else:
        if parent1.right and parent1.right == node1:
            parent1.right = node2

    # Swapping second node's parent link to node1
    if parent2.left and parent2.left == node2:
        parent2.left = node1
    elif parent2.right and parent2.right == node2:
        parent2.right = node1

    # Swapping children of node1 to node2
    if left1 or right1:
        if left1:
            node2.left = left1
        if right1:
            node2.right = right1
    if not left1 and not right1:
        node2.left = node2.right = None

    # Swapping children of node2 to node1
    if left2 or right2:
        if left2:
            node1.left = left2
        if right2:
            node1.right = right2
    if not left2 and not right2:
        node1.left = node1.right = None

    # print(root.data)
    # print(root.left.data)
    # print(root.right.data)
    # print(root.left.left.data)
    # print(root.left.right.data)
    # print(root.right.left.data)
    # print(root.right.right.data)
    return root


def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data, end=' ')
    inOrder(root.right)


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = node1 = newNode(3)
    root.left.left = node2 = newNode(7)
    root.left.right = newNode(6)
    root.right.left = newNode(5)
    root.right.right = newNode(4)
    newRoot = btSwap(root, node1, node2)
    inOrder(newRoot)
