class Order:
    def __init__(self,items,price):
        self.items = items
        self.price = price

    def __gt__(self,order2):
        if self.price > order2.price:
            print("order1 price is High: ",self.price)
        else:
            print('order2 price is hight')



order1 = Order("chips", 150)
order2 = Order('tea', 80)
print(order1>order2)