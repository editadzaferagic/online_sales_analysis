from product import Product
from product_manager import ProductManager

pm = ProductManager()
pm.add_product(Product("Laptop", 1200, 3))
pm.add_product(Product("Mouse", 25, 10))
pm.add_product(Product("Keyboard", 60, 4))

pm.show_all_products()
print("Total Inventory Value:", pm.total_inventory_value())