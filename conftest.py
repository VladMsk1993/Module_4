from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

"""Передача параметров через командную строку с помощью встроенной функции pytest_addoption и фикстуры request."""

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()  # Указываем язык браузера с помощью WebDriver, используя класс Options и метод add_experimental_option.
    print("\nstart chrome browser for test..")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  # Указываем что берётся язык пользователя.
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()