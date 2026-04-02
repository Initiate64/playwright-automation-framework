from playwright.sync_api import Page, expect

def test_add_to_cart(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Verify login
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # Add first item to cart
    page.click("button[id='add-to-cart-sauce-labs-backpack']")

    # Click cart icon
    page.click(".shopping_cart_link")

    # Verify item is in cart
    expect(page.locator(".cart_item")).to_have_count(1)
