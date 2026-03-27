import allure
import pytest
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelper

BASE_URL = 'https://ok.ru/'


@allure.suite('Проверка выпадающего списка')
@allure.title('Код страны в поле "Номер телефона" соответствует выбранной из списка')
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_registration()
    registration_page = RegistrationPageHelper(browser)
    selected_country_code = registration_page.select_random_country()
    actual_country_code = registration_page.get_phone_field_value()
    assert selected_country_code == actual_country_code
