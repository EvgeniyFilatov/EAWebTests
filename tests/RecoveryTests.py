import allure
import pytest
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper
from pages.RecoveryByPhonePage import RecoveryByPhonePageHelper
from pages.RecoveryByEmailPage import RecoveryByEmailPageHelper

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


@allure.suite('Проверяем восстановление пользователя')
@allure.title('Проверяем переход к восстановлению через телефон')
def test_go_to_recovery_by_phone(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_forgot_button()
    recovery_page = RecoveryPageHelper(browser)
    recovery_page.click_phone_button()
    RecoveryByPhonePageHelper(browser)


@allure.suite('Проверяем восстановление пользователя')
@allure.title('Проверяем переход у восстановлению через почту')
def test_go_to_recovery_by_email(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_forgot_button()
    recovery_page = RecoveryPageHelper(browser)
    recovery_page.click_email_button()
    RecoveryByEmailPageHelper(browser)
