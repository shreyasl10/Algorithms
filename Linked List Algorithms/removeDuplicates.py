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

    def removeDuplicates(self):
        ptr = self.head
        while ptr and ptr.next:
            if ptr.data == ptr.next.data:
                tempNode = ptr.next
                ptr.next = tempNode.next
                tempNode.next = None
            else:
                ptr = ptr.next


c = 1
l = List()
while(c != 0):
    n = int(input("Enter the value of the node you want to insert\n"))
    l.Insert(n)
    c = int(input("Enter 0 if you want to stop inserting and print the list. If you want to continue, Enter 1\n"))
l.PrintList()
l.removeDuplicates()
l.PrintList()
