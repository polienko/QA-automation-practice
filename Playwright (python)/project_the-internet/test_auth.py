import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_positive_auth(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":360,"height":740})
    page = context.new_page()
    page.locator("html").click()
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name=re.compile(r".*Login")).click()
    expect(page.get_by_text("You logged into a secure area")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()
