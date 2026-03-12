import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class RecoveryByPhonePageLocators:
    TITLE_LABEL = (By.XPATH, '//div[text()="Укажите телефон"]')
    PHONE_FIELD = (By.NAME, 'st.r.phone')
    COUNTRY_FIELD = (By.XPATH, '//div[@data-l="t,country"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')


class RecoveryByPhonePageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RecoveryByPhonePageLocators.TITLE_LABEL)
        self.find_element(RecoveryByPhonePageLocators.PHONE_FIELD)
        self.find_element(RecoveryByPhonePageLocators.COUNTRY_FIELD)
        self.find_element(RecoveryByPhonePageLocators.SUBMIT_BUTTON)
