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

    def PrintList(self, word=False):
        ptr = self.head
        if word == True:
            while ptr:
                print(ptr.data, end='')
                ptr = ptr.next
            return
        while ptr:
            print(ptr.data, end="->")
            ptr = ptr.next

    def Reverse(self):
        mBlank = []
        firstBlank = None
        ptr = self.head

        # Getting first occurence of blank to terminate link at the end
        while ptr.next.data != ' ':
            ptr = ptr.next
        firstBlank = ptr

        # Retrieving first and last nodes of the list
        ptr = self.head
        mBlank.append([ptr, ''])

        # Retrieving nodes that are blanks/spaces
        while ptr.next:
            if ptr.next.data == ' ':
                mBlank.append([ptr, ptr.next])
            ptr = ptr.next
        mBlank.append([ptr, ''])

        self.head = mBlank[len(mBlank)-2][1].next

        for i in range(len(mBlank)-1, -1, -1):
            if i-2 >= 0:
                if i == 2:
                    mBlank[i][0].next = mBlank[i-2][0]
                else:
                    mBlank[i][0].next = mBlank[i-2][1]
                print(mBlank[i][0].next.next.data)
            else:
                break

        # Setting the next part of the letter before the first space to None to mark the end of the new list
        firstBlank.next = None


c = 1
l = List()
inputString = list(input('Input Sentence: \n'))
for i in inputString:
    l.Insert(i)
print('Actual sentence:')
l.PrintList()
print('\nReversed sentence:')
l.Reverse()
l.PrintList()
