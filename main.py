from abc import abstractmethod

class CartIsEmptyException(Exception):
    def __init__(self):
        msg = "Cart is Empty. !! \nPlease add Items first."
        super().__init__(msg)

class AmountInvalidException(Exception):
    def __init__(self):
        msg = "Invalid Amount !! \nplease Enter valid amount."
        super().__init__(msg)


class DessrtIteam:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cost_of_item(self):
        pass

    def display_name(self):
        return self.name

class Candy(DessrtIteam):

    def __init__(self,name, weight):
        super().__init__(name)
        self.weightPer_gm = weight
        self.price_per_kg = 50

    def cost_of_item(self):
        return self.weightPer_gm * (self.price_per_kg / 1000)

class Cookie(DessrtIteam):

    def __init__(self, name, units):
        super().__init__(name)
        self.units = units
        self.price_per_dozzen = 10

    def cost_of_item(self):
        return self.units * (self.price_per_dozzen / 12)

class Icecreame(DessrtIteam):

    def __init__(self, name):
        super().__init__(name)
        self.price = 30

    def cost_of_item(self):
        return self.price

class Sundae(Icecreame):

    def __init__(self,name):
        super().__init__(name)
        self.cost_of_topping = 50

    def cost_of_item(self):
        return self.price + self.cost_of_topping

class Checkout:

    def __init__(self):
        self.dessert_items = []

    def add_items(self, *items):
        for i in items:
            self.dessert_items.append(i)

    def count_of_items(self):
        return len(self.dessert_items)

    def total_cost(self):
        if self.count_of_items() == 0:
            raise CartIsEmptyException
        else:
            # total_cost = 0
            # for i in self.dessert_items:
            #     total_cost += i.cost_of_item()
            # return total_cost
            return "{:.2f}".format(sum([i.cost_of_item() for i in self.dessert_items]))

    def __str__(self):
        empty = ""
        for i in self.dessert_items:
            empty = empty + "Name : " + i.display_name() + "\nCost : " + f"{i.cost_of_item():.2f}" + "\n\n"
        return empty


check = Checkout()

candy = Candy("Fudge", 200)
cookie = Cookie("Hide&Seek", 4)
ice = Icecreame("Chocolate")
sundae = Sundae("Vanila")

check.add_items()
print("Total Items in cart : ", check.count_of_items())
print(check)
try:
    print(check.total_cost())
except CartIsEmptyException as emp:
    print(emp)
