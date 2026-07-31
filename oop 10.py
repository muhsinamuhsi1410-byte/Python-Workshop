#store inventory list(list of objects)
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:

    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def total_inventory_value(self):
        total = 0

        for product in self.inventory:
            total += product.price * product.quantity

        return total

store = Store()

p1 = Product("Pen", 10, 5)
p2 = Product("Book", 50, 2)

store.add_product(p1)
store.add_product(p2)

print("Total Value =", store.total_inventory_value())