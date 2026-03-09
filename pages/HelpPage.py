import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class HelpPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@type="search"]')
    ACTUAL_TODAY_LINK = (By.XPATH, '//div[text()="Сегодня актуально"]')
    REGISTRATION_LINK = (By.XPATH, '//div[text()="Регистрация"]')
    MY_PROFILE_LINK = (By.XPATH, '//div[text()="Мой профиль"]')
    COMMUNICATION_LINK = (By.XPATH, '//div[text()="Общение"]')
    PROFILE_ACCESS_LINK = (By.XPATH, '//div[text()="Доступ к профилю"]')
    SECURITY_LINK = (By.XPATH, '//div[text()="Безопасность"]')
    GROUPS_LINK = (By.XPATH, '//div[text()="Группы"]')
    PAYED_FUNCTIONS_LINK = (By.XPATH, '//div[text()="Платные функции"]')
    SPAM_LINK = (By.XPATH, '//div[text()="Нарушения и спам"]')
    GAMES_AND_APPS_LINK = (By.XPATH, '//div[text()="Игры и приложения"]')
    OTHER_SERVICES_LINK = (By.XPATH, '//div[text()="Другие сервисы"]')
    USEFUL_INFORMATION_LINK = (By.XPATH, '//div[text()="Полезная информация"]')
    AD_CABINET_LINK = (By.XPATH, '//div[text()="Рекламный кабинет"]')


class HelpPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.SEARCH_FIELD)
        self.find_element(HelpPageLocators.ACTUAL_TODAY_LINK)
        self.find_element(HelpPageLocators.REGISTRATION_LINK)
        self.find_element(HelpPageLocators.MY_PROFILE_LINK)
        self.find_element(HelpPageLocators.COMMUNICATION_LINK)
        self.find_element(HelpPageLocators.PROFILE_ACCESS_LINK)
        self.find_element(HelpPageLocators.SECURITY_LINK)
        self.find_element(HelpPageLocators.GROUPS_LINK)
        self.find_element(HelpPageLocators.PAYED_FUNCTIONS_LINK)
        self.find_element(HelpPageLocators.SPAM_LINK)
        self.find_element(HelpPageLocators.GAMES_AND_APPS_LINK)
        self.find_element(HelpPageLocators.OTHER_SERVICES_LINK)
        self.find_element(HelpPageLocators.USEFUL_INFORMATION_LINK)
        self.find_element(HelpPageLocators.AD_CABINET_LINK)

    @allure.step('Скроллим до элемента')
    def scroll_to_item(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).perform()
        self.attach_screenshot()

    @allure.step('Наводим на элемент и кликаем')
    def move_to_item(self, locator):
        move_item = self.find_element(locator)
        ActionChains(self.driver).move_to_element(move_item).perform()
        self.attach_screenshot()
        move_item.click()
