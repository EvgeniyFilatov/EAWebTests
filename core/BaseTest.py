import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=ru")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Remote(command_executor="http://85.198.69.66:4444", options=options)
    yield driver
    driver.quit()
