class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def InsertLevel(arr, i, n):
    root = None
    if i < n:
        root = Node(arr[i])
        root.left = InsertLevel(arr, 2*i+1, n)
        root.right = InsertLevel(arr, 2*i+2, n)
    return root


def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data, end=' ')
    inOrder(root.right)


arr = list(map(int, input().split()))
newRoot = InsertLevel(arr, 0, len(arr))
inOrder(newRoot)
