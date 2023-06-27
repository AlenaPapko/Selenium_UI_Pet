from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return login_link

    def select_pets(self):
        select_pets = self.browser.find_element(*MainPageLocators.DROP_DOWN)
        select_pets.click()
        return select_pets

    def pet_cat(self):
        cat = self.browser.find_element(*MainPageLocators.CAT)
        cat.click()
        return cat

    def filter_name(self):
        self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME).send_keys('Chipa', Keys.ENTER)

