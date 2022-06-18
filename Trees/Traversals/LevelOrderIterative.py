class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def LevelOrder(root):
    if not root:
        return 
    order=[]
    ptr=[]
    ptr.append(root)
    while len(ptr):
        x=ptr.pop(0)
        order.append(x.data)
        if x.left:
            ptr.append(x.left)
        if x.right:
            ptr.append(x.right)
    return order
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print(LevelOrder(root))
