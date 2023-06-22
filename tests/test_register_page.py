import time

from pages.register_page import RegisterPageValid, RegisterPageEmpty


def test_register_valid(browser):
    link = 'http://34.141.58.52:8080/#/register'
    reg_page = RegisterPageValid(browser, link)
    reg_page.open()
    reg_page.register_login()
    reg_page.register_pass()
    reg_page.register_conf_pass()
    reg_page.register_btn_submit()
    time.sleep(3)
    browser.save_screenshot('result_register.png')


def test_register_empty(browser):
    link = 'http://34.141.58.52:8080/#/register'
    reg_page_empty = RegisterPageEmpty(browser, link)
    reg_page_empty.open()
    reg_page_empty.register_login_empty()
    reg_page_empty.register_pass_empty()
    reg_page_empty.register_conf_pass_empty()
    reg_page_empty.register_btn_submit()
    time.sleep(3)
    browser.save_screenshot('result_reg_empty.png')
