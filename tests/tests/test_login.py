from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.navigate("https://the-internet.herokuapp.com/login")
        login_page.login("tomsmith", "SuperSecretPassword!")

        assert "secure" in page.url

        browser.close()


def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.navigate("https://the-internet.herokuapp.com/login")
        login_page.login("wrong", "wrong")

        error = page.text_content("#flash")
        assert "Your username is invalid!" in error

        browser.close()
