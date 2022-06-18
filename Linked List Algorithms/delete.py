class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.ptr = None

    def Insert(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.ptr = self.head
        else:
            self.ptr.next = newNode
            self.ptr = self.ptr.next
            newNode.next = None

    def Delete(self, value):
        ptr = self.head.next
        prev = self.head

        if self.head.data == value:
            prev = None
            self.head = ptr
            return

        while ptr:
            if ptr.data == value:
                prev.next = ptr.next
                ptr = None
                break
            ptr = ptr.next
            prev = prev.next

    def PrintList(self):
        ptr = self.head
        while ptr:
            if not ptr.next:
                print(ptr.data)
            else:
                print(ptr.data, end="->")
            ptr = ptr.next


c = 1
l = List()
while(c != 0):
    n = int(input("Enter the value of the node you want to insert\n"))
    l.Insert(n)
    c = int(input("Enter 0 if you want to stop inserting and print the list. If you want to continue, Enter 1\n"))
l.PrintList()
d = int(input("\nEnter the value of the node you want to delete\n"))
l.Delete(d)
l.PrintList()
