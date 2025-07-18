from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_all_products(self):
        for p in self.products:
            p.display_info()

    def total_inventory_value(self):
        return sum(p.price * p.quantity for p in self.products)
    
    def remove_product(self, name):
        self.products = [p for p in self.products if p.name != name]