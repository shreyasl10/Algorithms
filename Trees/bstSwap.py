class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def bstInsert(root, data):
    if not root:
        return newNode(data)
    if root.data > data:
        return bstInsert(root.left, data)
    elif root.data < data:
        return bstInsert(root.right, data)
    return root


def inOrder(root):
    output = []
    ptr = root
    temp = []
    while True:
        if ptr:
            temp.append(ptr)
            ptr = ptr.left
        elif temp:
            output.append(temp[-1])
            ptr = temp.pop()
            ptr = ptr.right
        else:
            break
    return output


def bstSwap(root):
    pos = 0
    min_val = float('inf')
    min_ind = -1
    InOrderOut = inOrder(root)
    i = 0
    for i in range(1, len(InOrderOut)-1):
        if InOrderOut[i].data < InOrderOut[i-1].data:
            pos = i
    for j in range(i+1, len(InOrderOut)):
        if InOrderOut[j].data < min_val:
            min_val = InOrderOut[j].data
            min_ind = j
    InOrderOut[min_ind].data = InOrderOut[i].data
    InOrderOut[pos].data = min_val
    return InOrderOut


if __name__ == '__main__':
    root = None
    root = bstInsert(root, 3)
    root = bstInsert(root, 1)
    root = bstInsert(root, 4)
    root = bstInsert(root, 2)
    finalRoot = bstSwap(root)
    for i in finalRoot:
        print(i.data, end=' ')
