
# The question is to create a class called GoldInvoice with the below mentioned attributes and two methods- one to calculate the price of an item without including GST and one including GST.
# The arguments of the method are a list of GoldInvoice objects and the itemid for which we need to calculate the total price.
# The math for finding the total cost is as follows:
# cost=quantity*rate*weight
# To this cost, we must add the percentage of wastage(pwc) and also subtract the discount percentage(pdis). In case of including GST, we need to add an additional 3% to the cost.
# The final cost that we display in the main function should be :
# 1)with 3 decimal points in case of exGST
# 2)with 2 decimal points in case of inGST
# In the main function we shall get the input from the user and pass it into the list of goldinvoice objects and later call the two methods required for our operation.

# Sample Input
# 3
# 101
# chain
# 2
# 100
# 12
# 5
# 4
# 102
# ring
# 3
# 200
# 40
# 3
# 6
# 103
# bracelet
# 3
# 120
# 60
# 6
# 7
# 101

# Sample Output
# 2424.000
# 2496.00


class GoldInvoice:
    def __init__(self, id, name, qty, rate, weight, pwc, pdis):
        self.id = id
        self.name = name
        self.qty = qty
        self.rate = rate
        self.weight = weight
        self.pwc = pwc
        self.pdis = pdis

    def calc_Item_Price_exGST(self, items, id):
        cost = 0
        for i in items:
            if i.id == id:
                actualcost = (i.qty*i.rate*i.weight)
        cost = actualcost+((actualcost*i.pwc)/100)
        cost -= ((actualcost*i.pdis)/100)
        return cost

    def calc_Item_Price_inGST(self, items, id):
        cost = 0
        for i in items:
            if i.id == id:
                actualcost = (i.qty*i.rate*i.weight)
        cost = actualcost+((actualcost*i.pwc)/100)
        cost -= ((actualcost*i.pdis)/100)
        cost += ((actualcost*3)/100)
        return cost


if __name__ == "__main__":
    items = []
    # Creating two dictionaries that will be storing the total costs of all items in id:cost manner
    costExGST = {}
    costInGST = {}
    n = int(input())
    for i in range(n):
        id = int(input())
        name = input()
        qty = float(input())
        rate = float(input())
        weight = float(input())
        pwc = float(input())
        pdis = float(input())
        g = GoldInvoice(id, name, qty, rate, weight, pwc, pdis)
        items.append(g)
        # Finding out the cost of a particular item and then storing it in the respective dictionary in id:cost manner.
        cost1 = g.calc_Item_Price_exGST(items, id)
        costExGST[id] = cost1
        cost2 = g.calc_Item_Price_inGST(items, id)
        costInGST[id] = cost2
    item_id = int(input())
    print("{:.3f}".format(costExGST[item_id]))
    print("{:.2f}".format(costInGST[item_id]))
