class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Peek(temp):
    if len(temp) > 0:
        return temp[-1]
    return


def PostOrder(root):
    order = []
    temp = []
    while True:
        while root:
            if root.right:
                temp.append(root.right)
            temp.append(root)
            root = root.left
        root = temp.pop()
        if(root.right and Peek(temp) == root.right):
            temp.pop()
            temp.append(root)
            root = root.right
        else:
            order.append(root)
            root = None
        if len(temp) <= 0:
            break
    return order


def PostOrder2(root):
    stack = []
    output = []
    while True:
        while root:
            stack.append(root)
            stack.append(root)
            root = root.left

        if len(stack) == 0:
            return output

        root = stack.pop()

        if len(stack) > 0 and stack[-1] == root:
            root = root.right
        else:
            output.append(root)
            root = None


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(7)
a = PostOrder(root)
b = PostOrder2(root)
for i in range(len(a)):
    print(a[i].data, end=' ')
print()
for i in range(len(b)):
    print(b[i].data, end=' ')

# I have shared the letter regarding the company's reopening to the address of the following parties. They will contact you regarding order details.
# Thanking you
