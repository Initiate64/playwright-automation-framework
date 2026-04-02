from .base_page import BasePage

class InventoryPage(BasePage):
    ADD_BACKPACK = "button[id='add-to-cart-sauce-labs-backpack']"
    CART_ICON = ".shopping_cart_link"

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK)

    def go_to_cart(self):
        self.click(self.CART_ICON)
