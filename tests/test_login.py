from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Enter username
    page.fill("#user-name", "standard_user")

    # Enter password
    page.fill("#password", "secret_sauce")

    # Click login button
    page.click("#login-button")

    # Verify successful login by checking the page URL or an element on the next page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
