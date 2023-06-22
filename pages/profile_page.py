from .base_page import BasePage
from .locators import ProfilePageLocators


class AddPet(BasePage):
    def add_new_pet(self):
        add_pet = self.browser.find_element(*ProfilePageLocators.CREATE_PET)
        add_pet.click()
        return add_pet

    def add_name(self):
        name = self.browser.find_element(*ProfilePageLocators.NAME)
        name.send_keys('Rio')
        return name

    def add_age(self):
        age = self.browser.find_element(*ProfilePageLocators.AGE)
        age.send_keys('44')
        return age

    def add_type_pet(self):
        type_pet = self.browser.find_element(*ProfilePageLocators.TYPE)
        type_pet.click()

    def dog_type(self):
        pet_dog = self.browser.find_element(*ProfilePageLocators.DOG).click()

    def pet_btn(self):
        submit_btn = self.browser.find_element(*ProfilePageLocators.PET_BTN)
        submit_btn.submit()

    def edit_pets(self):
        edit_btn = self.browser.find_element(*ProfilePageLocators.EDIT_BTN)
        edit_btn.click()

    def delete_btn(self):
        delete_btn = self.browser.find_element(*ProfilePageLocators.DELETE_BTN)
        delete_btn.click()

    def delete_no_btn(self):
        delete_no_btn = self.browser.find_element(*ProfilePageLocators.BTN_NO_DELETE)
        delete_no_btn.click()

    def edit_name(self):
        edit_name = self.browser.find_element(*ProfilePageLocators.NAME)
        edit_name.send_keys('Chi')

    def save_button(self):
        save_button = self.browser.find_element(*ProfilePageLocators.SAVE_BTN)
        save_button.submit()

    def quit_btn(self):
        quit_btn = self.browser.find_element(*ProfilePageLocators.QUIT_BTN)
        quit_btn.click()
        return quit_btn

