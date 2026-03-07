import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelpers, HelpPageLocators
from pages.AdvertisingCabPage import AdvertisingCabPageHelper

BASE_URL = 'https://ok.ru/help'

@allure.suite('Проверка раздела "Помощь"')
@allure.title('Проверка перехода к категории "Рекламный кабинет')
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    help_page = HelpPageHelpers(browser)
    help_page.scroll_to_item(HelpPageLocators.AD_CABINET_LINK)
    help_page.move_to_item(HelpPageLocators.AD_CABINET_LINK)
    AdvertisingCabPageHelper(browser)