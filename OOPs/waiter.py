class Table:
    def __init__(self, no, name, status):
        self.no = no
        self.name = name
        self.status = status

    def findWaiterTotal(self, tables):
        d = {}
        for i in tables:
            d[i.name] = 0
        for i in tables:
            d[i.name] += 1
        return d

    def findName(self, tables, num):
        for i in tables:
            if i.no == num:
                return i.name
        return


if __name__ == '__main__':
    n = int(input())
    tables = []
    for i in range(n):
        no = int(input())
        name = input()
        status = input()
        tables.append(Table(no, name, status))
    t = Table(0, 'a', 'a')
    num = int(input())
    output = t.findWaiterTotal(tables)
    l = list(output.keys())
    l.sort()
    for i in l:
        print(f"{i} {output[i]}")
    name = t.findName(tables, num)
    if name == None:
        print("No Table Found")
    else:
        print(name)
