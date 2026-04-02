from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_swag_labs_flow(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    # Step 1: Go to login page
    login_page.goto("https://www.saucedemo.com/")

    # Step 2: Login
    login_page.login("standard_user", "secret_sauce")

    # Step 3: Add item to cart
    inventory_page.add_backpack_to_cart()

    # Step 4: Go to cart
    inventory_page.go_to_cart()

    # Step 5: Verify cart has 1 item
    cart_page.verify_item_count(1)
