import pytest, re
from playwright.sync_api import Playwright, sync_playwright, expect



 
def test_booking(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":360,"height":740})
    page = context.new_page()
    page.goto("https://automationintesting.online/")
    page.get_by_role("heading", name="Single").click()
    page.locator("div").filter(has_text=re.compile(r"^£100 per nightBook now$")).get_by_role("link").click()
    page.get_by_role("button", name="Reserve Now").click()
    page.get_by_placeholder("Firstname").click()
    page.get_by_placeholder("Firstname").fill("hvx-first")
    page.get_by_placeholder("Firstname").press("Tab")
    page.get_by_placeholder("Lastname").fill("hvx-last")
    page.get_by_placeholder("Lastname").press("Tab")
    page.get_by_placeholder("Email").fill("hvx@test.ru")
    page.get_by_placeholder("Email").press("Tab")
    page.get_by_placeholder("Phone").fill("12345678901")
    page.get_by_role("button", name="Reserve Now").click()
    page.get_by_role("button").first.click()
    page.get_by_role("link", name="Admin", exact=True).click()
    page.get_by_placeholder("Enter username").click()
    page.get_by_placeholder("Enter username").fill("admin")
    page.get_by_placeholder("Enter username").press("Tab")
    page.get_by_placeholder("Password").fill("password")
    page.get_by_role("button", name="Login").click()
    page.get_by_label("Toggle navigation").click()
    page.get_by_label("Toggle navigation").click()
    expect(page.get_by_role("link", name="Restful Booker Platform Demo")).to_be_visible()