from playwright.sync_api import Page, expect
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME_INPUT = "[name='username']"
    PASSWORD_INPUT = "[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    SUCCESS_MESSAGE = "text=You logged into a secure area"
    ERROR_MESSAGE = "text=Your username is invalid!"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_login(self):
        self.navigate(self.URL)
    
    def fill_username(self, username: str):
        self.page.fill(self.USERNAME_INPUT, username)
        return self
    
    def fill_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)
        return self
    
    def click_login(self):
        self.page.click(self.LOGIN_BUTTON)
    
    def login(self, username: str, password: str):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
    
    def is_success_message_visible(self) -> bool:
        try:
            expect(self.page.locator(self.SUCCESS_MESSAGE)).to_be_visible()
            return True
        except:
            return False
    
    def is_error_message_visible(self) -> bool:
        try:
            expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()
            return True
        except:
            return False