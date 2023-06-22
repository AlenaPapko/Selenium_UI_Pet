import time

import pytest

from pages.login_page import LoginPage, InvalidLogin


@pytest.mark.smoke
def test_valid_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_pass()
    page.go_to_button()
    time.sleep(3)
    browser.save_screenshot('result_valid.png')


def test_invalid_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page2 = InvalidLogin(browser, link)
    page2.open()
    page2.go_to_invalid_login()
    page2.go_to_invalid_pass()
    page2.go_to_button()
    time.sleep(3)
    browser.save_screenshot('result_invalid.png')
