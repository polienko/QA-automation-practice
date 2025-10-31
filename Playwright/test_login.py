import pytest
from pages.login_page import LoginPage


class TestLogin:
    VALID_USERNAME = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"
    INVALID_USERNAME = "wrong_username"
    INVALID_PASSWORD = "wrong_password"
    
    def test_positive_auth(self, login_page: LoginPage):
        """Тест успешной авторизации"""
        login_page.login(self.VALID_USERNAME, self.VALID_PASSWORD)

        assert login_page.is_success_message_visible()
    
    def test_bad_credentials(self, login_page: LoginPage):
        """Тест с неверными учетными данными"""

        login_page.login(self.INVALID_USERNAME, self.INVALID_PASSWORD)

        assert login_page.is_error_message_visible()
    
    def test_empty_credentials(self, login_page: LoginPage):
        """Тест с пустыми полями"""
        login_page.login("", "")

        assert login_page.is_error_message_visible()