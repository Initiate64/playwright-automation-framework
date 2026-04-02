from playwright.sync_api import expect
from .base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = ".cart_item"

    def verify_item_count(self, count: int):
        expect(self.page.locator(self.CART_ITEM)).to_have_count(count)
