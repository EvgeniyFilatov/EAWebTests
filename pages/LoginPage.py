from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_CODE = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@label="Войти"]')
    LOGIN_BY_QR_CODE = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    FORGOT_BUTTON = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    REGISTER_BUTTON = (By.XPATH, '//span[text()="Зарегистрироваться"]')
    VK_ID_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_ID_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')


class LoginPageHelper(BasePage):
    pass

