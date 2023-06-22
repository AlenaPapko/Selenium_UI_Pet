import pytest
from selenium import webdriver
from pages.data import LoginData
from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def go_to_login(browser):
    link = LoginData.LOGIN_PAGE_LINK
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_pass()
    page.go_to_button()
