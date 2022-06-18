class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def Insert(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = newNode
            newNode.next = None

    def PrintList(self):
        ptr = self.head
        while ptr:
            if not ptr.next:
                print(ptr.data)
            else:
                print(ptr.data, end="->")
            ptr = ptr.next

    def mergeSorted(self, head2):
        output = List()
        ptr1 = self.head
        ptr2 = head2

        while ptr1 and ptr2:
            outNode = None
            if ptr1.data <= ptr2.data:
                outNode = ptr1
                ptr1 = ptr1.next
            else:
                outNode = ptr2
                ptr2 = ptr2.next

            output.Insert(outNode.data)

        while ptr1:
            output.Insert(ptr1.data)
            ptr1 = ptr1.next

        while ptr2:
            output.Insert(ptr2.data)
            ptr2 = ptr2.next

        output.PrintList()


l1 = List()
while(True):
    n = int(input("Enter the value of the node you want to insert for list 1\n"))
    if n == -1:
        break
    l1.Insert(n)
l1.PrintList()

l2 = List()
while(True):
    n = int(input("Enter the value of the node you want to insert for list 2\n"))
    if n == -1:
        break
    l2.Insert(n)
l2.PrintList()

l1.mergeSorted(l2.head)
