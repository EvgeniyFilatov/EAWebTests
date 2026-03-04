import random
import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//div[@data-l="t,phone"]')
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')
    REGULATIONS_LINK = (By.XPATH, '//a[@data-l="t,agreement"]')
    PRIVACY_LINK = (By.XPATH, '//a[@data-l="t,privacy"]')


class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.PHONE_FIELD)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST)
        self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
        self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)
        self.find_element(RegistrationPageLocators.REGULATIONS_LINK)
        self.find_element(RegistrationPageLocators.PRIVACY_LINK)

    @allure.step('Выбираем рандомную страну из списка')
    def select_random_country(self):
        random_number = random.randint(0, 212)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_code = country_items[random_number].get_attribute('text')
        country_items[random_number].click()
        self.attach_screenshot()
        return country_code

    @allure.step('Получаем значение поля "Номер телефона"')
    def get_phone_field_value(self):
        self.attach_screenshot()
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')
