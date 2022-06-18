class Product:
    def __init__(self, id, name, type, price):
        self.id = id
        self.name = name
        self.type = type
        self.price = price

    def apply_discount(self, num):
        self.price -= (self.price*num)/100


class Store:
    def __init__(self, name, prods):
        self.name = name
        self.prods = prods

    def calculate_price(self, type, num):
        result = []
        for i in self.prods:
            if i.type == type:
                i.apply_discount(num)
                result.append(i)
        if len(result) == 0:
            return None
        return sorted(result, key=lambda i: i.price, reverse=True)


n = int(input())
products = []
for i in range(n):
    id = int(input())
    name = input()
    type = input()
    price = int(input())
    products.append(Product(id, name, type, price))
s = Store('ABC', products)
prodtype = input()
amount = int(input())
result = s.calculate_price(prodtype, amount)
if len(result) == 0:
    print("Product Not Found")
else:
    for i in result:
        print(f"{i.name} {i.price}")
