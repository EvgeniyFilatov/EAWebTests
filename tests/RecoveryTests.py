import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper

BASE_URL = 'https://ok.ru/'


@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода к восстановлению после нескольких неудачных попыток авторизации')
def test_go_to_recovery_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.input_login('email')

    for _ in range(2):
        login_page.input_password('123')
        login_page.click_login()
        login_page.get_error_text()

    login_page.input_password('123')
    login_page.click_login()

    login_page.click_recovery()
    RecoveryPageHelper(browser)
