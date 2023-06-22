import time

import pytest

from pages.profile_page import AddPet
from pages.data import ProfileData


@pytest.mark.smoke
def test_add_new_pets(browser, go_to_login):
    link = ProfileData.PROFILE_LINK
    add_pet = AddPet(browser, link)
    add_pet.open()
    add_pet.add_new_pet()
    add_pet.add_name()
    add_pet.add_age()
    add_pet.add_type_pet()
    add_pet.dog_type()
    add_pet.pet_btn()
    time.sleep(3)
    browser.save_screenshot('result_add.png')


def test_edit_pet(browser, go_to_login):
    link = ProfileData.PROFILE_LINK
    edit = AddPet(browser, link)
    edit.open()
    edit.edit_pets()
    edit.edit_name()
    edit.save_button()
    time.sleep(3)
    browser.save_screenshot('result_edit.png')


def test_delete_pet(browser, go_to_login):
    link = ProfileData.PROFILE_LINK
    delete = AddPet(browser, link)
    delete.open()
    delete.delete_btn()
    delete.delete_no_btn()
    time.sleep(3)
    browser.save_screenshot('result_delete.png')


def test_quit_button(browser, go_to_login):
    link = ProfileData.PROFILE_LINK
    quit_button = AddPet(browser, link)
    quit_button.open()
    quit_button.quit_btn()
    time.sleep(3)
    browser.save_screenshot('result_quit.png')
