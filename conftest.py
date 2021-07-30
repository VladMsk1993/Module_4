from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

"""Передача параметров через командную строку с помощью встроенной функции pytest_addoption и фикстуры request."""
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox") # default откроет поулмолчанию хромбраузер.
    parser.addoption('--language', action='store', default="en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options() #Указываем язык браузера с помощью WebDriver, используя класс Options и метод add_experimental_option.
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) # Указываем что берётся язык пользователя.
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()
