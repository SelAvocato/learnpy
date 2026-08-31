class InventoryManager:
    def __init__(self, products_by_id, products_by_categories, product_last_id):
        self.products_by_id = products_by_id
        self.products_by_categories = products_by_categories
        self.product_last_id = product_last_id

    def handle_error(self, e):
        print(f"Error: ${e}")

    def increment_id(self):
        try:
            self.product_last_id += 1
            return self.product_last_id
        except:
            return 1

    def add_product(self, name, quantity=0, category="Uncategorized"):
        try:
            new_id = self.increment_id()
            new_product = {
                "id": new_id,
                "name": name,
                "quantity": quantity,
                "category": category,
            }
            self.products_by_id[new_id] = new_product
            if category not in self.products_by_categories:
                self.products_by_categories[category] = []
            self.products_by_categories[category].append(new_product)
        except Exception as e:
            self.handle_error(e)

    def add_multiple_products(self, *items):
        try:
            for item in items:
                self.add_product(
                    item.get("name", ""),
                    item.get("quantity", 0),
                    item.get("category", "Uncategorized"),
                )
        except Exception as e:
            self.handle_error(e)

    def update_item(self, id, **item_info):
        try:
            product = self.products_by_id[id]
            if "category" in item_info:
                new_category = item_info.get("category")
                old_category = product["category"]

                if new_category != old_category:
                    categories = self.products_by_categories

                    if old_category in categories:
                        categories[old_category].remove(product)

                    if new_category not in categories:
                        categories[new_category] = []
                    categories[new_category].append(product)

            product.update(item_info)
        except Exception as e:
            self.handle_error(e)

    def delete_product(self, id):
        try:
            if self.products_by_id.get(id) is None:
                print("Product does not exist")
                return

            target_product = self.products_by_id[id]
            target_product_category = target_product.get("category")
            for index, product in enumerate(
                self.products_by_categories[target_product_category]
            ):
                if product.get("id") == id:
                    del self.products_by_categories[target_product_category][index]
                    break
            del self.products_by_id[id]
        except Exception as e:
            self.handle_error(e)

    def get_low_stock_products(self, threshold):
        return [
            val
            for val in self.products_by_id.values()
            if val.get("quantity", 0) <= threshold
        ]

    def get_categories(self):
        return list(self.products_by_categories)

    def print_report(self):
        for product in self.products_by_id.values():
            print(
                f"#{product.get("id")} | {product.get('name')} | {product.get('quantity')} units | {product.get('category')}"
            )
