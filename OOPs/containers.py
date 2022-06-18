class Container:
    def __init__(self, id, length, breadth, height, price):
        self.id = id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.price = price

    def findVolume(self):
        return self.length*self.breadth*self.height


class PackagingCompany:
    def __init__(self, containers):
        self.containers = containers

    def findContainerCost(self, id):
        for i in self.containers:
            if i.id == id:
                return i.findVolume()*i.price
        return None

    def findLargestContainer(self):
        m = self.containers[0].findVolume()
        obj = self.containers[0]
        for i in self.containers:
            if i.findVolume() > m:
                m = i.findVolume()
                obj = i
        return obj


if __name__ == '__main__':
    n = int(input())
    containers = []
    for i in range(n):
        id = int(input())
        l = int(input())
        b = int(input())
        h = int(input())
        p = int(input())
        containers.append(Container(id, l, b, h, p))
    p = PackagingCompany(containers)
    cost = p.findContainerCost(containers)
    if cost == None:
        print("No container found")
    else:
        print(cost)
    m = p.findLargestContainer()
    print(f"{m.id} {m.findVolume()}")
