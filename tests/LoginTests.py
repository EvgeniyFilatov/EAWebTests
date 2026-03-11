import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://ok.ru/'
LOGIN_TEXT = 'username'
WRONG_PASSWORD = '123'
EMPTY_LOGIN_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'
WRONG_PASSWORD_ERROR = 'Неправильно указан логин и/или пароль'


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_empty_login_and_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_LOGIN_ERROR


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустом поле "Password"')
def test_empty_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.input_login(LOGIN_TEXT)
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_PASSWORD_ERROR


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при неверном пароле')
def test_wrong_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.input_login(LOGIN_TEXT)
    login_page.input_password(WRONG_PASSWORD)
    login_page.click_login()
    assert login_page.get_error_text() == WRONG_PASSWORD_ERROR
