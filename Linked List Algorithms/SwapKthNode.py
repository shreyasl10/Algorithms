class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def InsertAtLast(self, i):
        n = Node(i)
        if not self.head:
            self.head = n
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = n
        n.next = None

    def PrintList(self):
        ptr = self.head
        while ptr:
            if not ptr.next:
                print(ptr.data)
            else:
                print(ptr.data, end="->")
            ptr = ptr.next

    def Swap(self, k):
        ptr1 = self.head
        ptr2 = self.head
        p = self.head
        p1 = self.head
        p2 = self.head
        n = 0
        while(p):
            n += 1
            p = p.next
        c = 1
        while(c != k):
            ptr1 = ptr1.next
            c += 1
        c = 1
        while(c != ((n-k)+1)):
            ptr2 = ptr2.next
            c += 1
        if k == 1:
            while p2.next != ptr2:
                p2 = p2.next
            ptr2.next = p1.next
            p2.next = p1
            p1.next = None
            self.head = ptr2
        elif k == n:
            while p1.next != ptr1:
                p1 = p1.next
            ptr1.next = ptr2.next
            p1.next = ptr2
            ptr2.next = None
            self.head = ptr1
        else:
            p = None
            while p1.next != ptr1:
                p1 = p1.next
            while p2.next != ptr2:
                p2 = p2.next
            p = ptr2.next
            p1.next = ptr2
            ptr2.next = ptr1.next
            ptr1.next = p
            p2.next = ptr1


l = List()
i = 0
while i != -1:
    i = int(input("Enter element to be inserted(Enter -1 to exit): "))
    l.InsertAtLast(i)
k = int(input("Enter the value of K\n"))
l.Swap(k)
l.PrintList()
