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
            newNode.next = self.head
            self.head = newNode

    def PrintList(self):
        ptr = self.head
        while ptr:
            if not ptr.next:
                print(ptr.data)
            else:
                print(ptr.data, end="->")
            ptr = ptr.next

    def Cycle(self):
        f = self.head
        s = self.head
        if not self.head or not self.head.next:
            return False
        while f and f.next:
            if f == s:
                s = self.head
                while(f != s):
                    f = f.next
                    s = s.next
                return f
            f = f.next.next
            s = s.next
        return False


c = 1
l = List()
while(c != 0):
    n = int(input("Enter the value of the node you want to insert\n"))
    l.Insert(n)
    c = int(input("Enter 0 if you want to stop inserting and print the list. If you want to continue, Enter 1\n"))
l.Cycle()
l.PrintList()
