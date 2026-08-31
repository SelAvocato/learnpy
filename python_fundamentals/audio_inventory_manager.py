from inventory_manager import InventoryManager


class AudioInventoryManager(InventoryManager):
    def __init__(self, products_by_id, product_last_id, products_by_tag):
        super().__init__(products_by_id, product_last_id=product_last_id)
        self.products_by_tag = products_by_tag

    def get_wireless(self):
        return self.products_by_tag["wireless"]
