#import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


#@pytest.mark.login
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ssp.smartyads.com/signin")
    page.get_by_role("tab", name="Login").click()
    page.get_by_label("E-mail*").click()
    page.get_by_label("E-mail*").fill("dobilim278@gronasu.com")
    page.get_by_label("Password*").click()
    page.get_by_label("Password*").fill("dobilim278")
    page.get_by_role("button", name="Login").click()


    expect(page.get_by_text("dobilim278@gronasu.com")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()




def test_login():
    with sync_playwright() as playwright:
        run(playwright)




