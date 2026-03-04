import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@label="Войти"]')
    LOGIN_BY_QR_CODE = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    FORGOT_BUTTON = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    REGISTRATION_BUTTON = (By.XPATH, '//span[text()="Зарегистрироваться"]')
    VK_ID_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_ID_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[contains(@class, "LoginForm-module__error")]')
    RESTORE_BUTTON = (By.XPATH, '//a[contains(@href, "anonymRecoveryStart")]')
    CANCEL_BUTTON = (By.XPATH, '//span[text()="Отмена"] ')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_QR_CODE)
        self.find_element(LoginPageLocators.FORGOT_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_ID_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.MAIL_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_ID_LOGIN_BUTTON)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
        self.attach_screenshot()

    @allure.step('Получаем ошибку')
    def get_error_text(self):
        error_element = self.find_element(LoginPageLocators.ERROR_TEXT).text
        self.attach_screenshot()
        return error_element

    @allure.step('Заполняем поле "Логин"')
    def input_login(self, *values):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(values)
        self.attach_screenshot()

    @allure.step('Заполняем поле "Пароль"')
    def input_password(self, *values):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).clear()
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(values)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.find_element(LoginPageLocators.RESTORE_BUTTON).click()
        self.attach_screenshot()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()
