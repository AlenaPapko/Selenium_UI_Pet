import time

from pages.main_page import MainPage


def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(3)
    browser.save_screenshot('result_log.png')


def test_select_pets(browser):
    link = 'http://34.141.58.52:8080/#/'
    sel_pets = MainPage(browser, link)
    sel_pets.open()
    sel_pets.select_pets()
    sel_pets.pet_cat()
    sel_pets.filter_name()
    time.sleep(3)
    browser.save_screenshot('select_pet.png')
