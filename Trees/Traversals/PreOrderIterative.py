class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
def PreOrder(root):
	if not root:
		return
	ptr=[]
	ptr.append(root)
	order=[]
	while(len(ptr)>0):
		x=ptr.pop()
		order.append(x)
		if x.right:
			ptr.append(x.right)
		if x.left:
			ptr.append(x.left)
	return order
root = Node(10) 	
root.left = Node(8) 	
root.right = Node(2) 	
root.left.left = Node(3) 	
root.left.right = Node(5) 
root.right.left = Node(2) 
a=PreOrder(root)
for i in range(len(a)):
	print(a[i].data,end=' ')

