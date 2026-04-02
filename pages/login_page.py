from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    def login(self, username: str, password: str):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        self.expect_url(self.INVENTORY_URL)
