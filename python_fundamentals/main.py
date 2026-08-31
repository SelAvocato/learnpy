from inventory_manager import InventoryManager

products_by_id = {
    1: {"id": 1, "name": "Keyboard", "quantity": 13, "category": "peripherals"},
    2: {"id": 2, "name": "Mouse", "quantity": 60, "category": "peripherals"},
    3: {"id": 3, "name": "Monitor", "quantity": 25, "category": "display"},
    4: {"id": 4, "name": "USB Flash Drive", "quantity": 120, "category": "storage"},
    5: {"id": 5, "name": "External Hard Drive", "quantity": 15, "category": "storage"},
}

products_by_categories = {
    "peripheral": [products_by_id[1], products_by_id[2]],
    "display": [products_by_id[3]],
    "storage": [products_by_id[4], products_by_id[5]],
}

product_last_id = 5

inventory = InventoryManager(products_by_id, products_by_categories, product_last_id)

inventory.add_multiple_products(
    {"name": "ror"},
    {"name": "dino", "quantity": 12},
    {"name": "item", "quantity": 100, "category": "ancient"},
)
inventory.add_product("Something")
inventory.add_product("Anything", 42)
inventory.add_product("I dunno", 32, "secret")
inventory.print_report()
inventory.update_item(1, name="touchpad")
inventory.update_item(2, name="phone", quantity=13, category="mobile device")
inventory.delete_product(3)
inventory.print_report()
print(
    "------------------------------------------Low Stock Products------------------------------------------"
)
for product in inventory.get_low_stock_products(20):
    print(
        f"#{product.get("id")} | {product.get('name')} | {product.get('quantity')} units | {product.get('category')}"
    )

print(inventory.get_categories())


# products_by_id = [
#     {"id": 1, "name": "Keyboard", "quantity": 13, "category": "Peripherals"},
#     {"id": 2, "name": "Mouse", "quantity": 60, "category": "Peripherals"},
#     {"id": 3, "name": "Monitor", "quantity": 25, "category": "Display"},
#     {"id": 4, "name": "USB Flash Drive", "quantity": 120, "category": "Storage"},
#     {"id": 5, "name": "External Hard Drive", "quantity": 15, "category": "Storage"},
# ]

# SUPPLIER = ({"name": "Acme Corp", "city": "Manila", "code": "011234"},)


# def print_error():
#     print("Something went wrong")


# def increment_id(products_list):
#     try:
#         latest_id = products_list[-1]["id"]
#         new_id = latest_id + 1
#         return new_id
#     except:
#         new_id = 1
#         return new_id


# def add_product(products_list, name, quantity, category="Uncategorized"):
#     new_id = increment_id(products_list)
#     try:
#         products_list.append(
#             {"id": new_id, "name": name, "quantity": quantity, "category": category}
#         )
#     except:
#         print_error()


# def add_multiple_products(products_list, *items):
#     for item in items:
#         new_id = increment_id(products)
#         name, quantity = item["name"], item["quantity"]
#         try:
#             if item["category"].strip() == "":
#                 raise ValueError
#             category = item["category"]
#         except:
#             category = "Uncategorized"

#         products_list.append(
#             {"id": new_id, "name": name, "quantity": quantity, "category": category}
#         )


# def update_product(products_list, id, **item):
#     for product in products_list:
#         if product["id"] == id:
#             product.update(item)
#         else:
#             continue


# def get_low_stock_products(products_list, threshold):
#     low_stock_products = []
#     for product in products_list:
#         if product["quantity"] <= threshold:
#             low_stock_products.append(product)

#     return low_stock_products


# def get_categories(products_list):
#     categories = []
#     for product in products_list:
#         categories.append(product["category"])

#     return set(categories)


# def print_report(products_list):
#     for product in products_list:
#         print(
#             f"{product["name"]} | {product["quantity"]} units | {product["category"]}"
#         )


# add_product(products, "Headphones", 43, "Audio")
# add_product(products, "Microphone", 21, "Audio")
# add_multiple_products(
#     products,
#     {"name": "Something", "quantity": 12},
#     {"name": "Anything", "quantity": 15, "category": ""},
# )
# print(products)

# update_product(products, 3, name="Jose", quantity=3333)

# print(products)
# print_report(products)
# print("lower than 30 stocks products: ", get_low_stock_products(products, 30))
# print(get_categories(products))
