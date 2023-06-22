from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    DROP_DOWN = (By.CLASS_NAME, 'p-dropdown-trigger')
    CAT = (By.ID, 'pv_id_2_1')
    FILTER_BY_PET_NAME = (By.ID, 'petName')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class RegisterPageLocators:
    REGISTER_EMAIL = (By.ID, 'login')
    REGISTER_PASS = (By.CSS_SELECTOR, '#password > input')
    REGISTER_CONF_PASS = (By.CSS_SELECTOR, '#confirm_password > input')
    REGISTER_BTN_SUBMIT = (By.CLASS_NAME, 'p-button-label')


class ProfilePageLocators:
    CREATE_PET = (By.CSS_SELECTOR, '.pi-plus')
    NAME = (By.ID, 'name')
    AGE = (By.CSS_SELECTOR, '#age > input')
    TYPE = (By.CSS_SELECTOR, '#typeSelector')
    DOG = (By.XPATH, '//*[@aria-label="dog"]')
    PET_BTN = (By.CSS_SELECTOR, '.p-button-success > .p-button-label')
    EDIT_PET = (By.CLASS_NAME, 'p-button p-component')
    EDIT_BTN = (By.CSS_SELECTOR, 'div#app > main > div > div > div:nth-of-type(2) > div > div > div > '
                                 'div:nth-of-type(2) > button')
    DELETE_BTN = (By.CSS_SELECTOR, ".col-12:nth-child(1) .p-button-danger")
    BTN_NO_DELETE = (By.CSS_SELECTOR, 'html > body > div:nth-of-type(3) > div:nth-of-type(2) > button > span')
    SAVE_BTN = (By.CSS_SELECTOR, 'div#app > main > div > form > div > div:nth-of-type(2) > div:nth-of-type(3) > button')
    QUIT_BTN = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a')
