from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPageValid(BasePage):
    def register_login(self):
        input_register_login = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        input_register_login.send_keys('test111@gmai.com')
        return input_register_login

    def register_pass(self):
        input_register_pass = self.browser.find_element(*RegisterPageLocators.REGISTER_PASS)
        input_register_pass.send_keys('111111')
        return input_register_pass

    def register_conf_pass(self):
        input_conf_pass = self.browser.find_element(*RegisterPageLocators.REGISTER_CONF_PASS)
        input_conf_pass.send_keys('111111')
        return input_conf_pass

    def register_btn_submit(self):
        register_btn = self.browser.find_element(*RegisterPageLocators.REGISTER_BTN_SUBMIT)
        register_btn.submit()
        return register_btn


class RegisterPageEmpty(BasePage):
    def register_login_empty(self):
        input_register_login_empty = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        input_register_login_empty.send_keys('      ')
        return input_register_login_empty

    def register_pass_empty(self):
        input_register_pass_empty = self.browser.find_element(*RegisterPageLocators.REGISTER_PASS)
        input_register_pass_empty.send_keys('      ')
        return input_register_pass_empty

    def register_conf_pass_empty(self):
        input_conf_pass_empty = self.browser.find_element(*RegisterPageLocators.REGISTER_CONF_PASS)
        input_conf_pass_empty.send_keys('     ')
        return input_conf_pass_empty

    def register_btn_submit(self):
        register_btn = self.browser.find_element(*RegisterPageLocators.REGISTER_BTN_SUBMIT)
        register_btn.submit()
        return register_btn
