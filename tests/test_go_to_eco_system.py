import allure
import pytest
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKEcosystemPage import VKEcosystemPageHelper

BASE_URL = 'https://ok.ru/'


@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экоситсемы VK')
def test_open_vk_ecosystem(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    first_window_id = login_page.get_window_id(0)
    login_page.click_vk_ecosystem()
    login_page.click_more_button()
    second_window_id = login_page.get_window_id(1)
    login_page.switch_window(second_window_id)
    vk_ecosystem_page = VKEcosystemPageHelper(browser)
    vk_ecosystem_page.switch_window(first_window_id)
    LoginPageHelper(browser)
