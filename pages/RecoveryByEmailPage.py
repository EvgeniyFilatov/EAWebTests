import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class RecoveryByEmailPageLocators:
    TITLE_LABEL = (By.XPATH, '//div[text()="Почта"]')
    EMAIL_FIELD = (By.XPATH, '//div[@data-l="t,email"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')


class RecoveryByEmailPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RecoveryByEmailPageLocators.TITLE_LABEL)
        self.find_element(RecoveryByEmailPageLocators.EMAIL_FIELD)
        self.find_element(RecoveryByEmailPageLocators.SUBMIT_BUTTON)
