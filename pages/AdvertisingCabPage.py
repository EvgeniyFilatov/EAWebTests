import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class AdvertisingCabPageLocators:
    TITLE = (By.XPATH, '//span[text()="Рекламный кабинет"]')


class AdvertisingCabPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(AdvertisingCabPageLocators.TITLE)
