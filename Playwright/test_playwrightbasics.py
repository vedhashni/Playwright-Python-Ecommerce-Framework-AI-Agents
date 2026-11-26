

from playwright.sync_api import sync_playwright
from playwright.async_api import Page

def test_launchdemo(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

#used run 
def test_launchdemo2(page:Page):
    page.goto("https://www.rahulshettyacademy.com")