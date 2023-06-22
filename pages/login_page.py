from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('papkotesta@gmail.com')
        return login_email

    def go_to_pass(self):
        input_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        input_pass.send_keys('Test1209')
        return input_pass

    def go_to_button(self):
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        button.submit()
        return button


class InvalidLogin(BasePage):

    def go_to_invalid_login(self):
        invalid_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        invalid_email.send_keys('1111')
        return invalid_email

    def go_to_invalid_pass(self):
        input_invalid_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        input_invalid_pass.send_keys('!!!')
        return input_invalid_pass

    def go_to_button(self):
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        button.submit()
        return button

