import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture(scope="function")
def browser_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 360, "height": 740})
    
    yield context
    
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def page(browser_context) -> Page:
    return browser_context.new_page()


@pytest.fixture(scope="function")
def login_page(page: Page):
    from pages.login_page import LoginPage
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    return login_page