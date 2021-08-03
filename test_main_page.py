from .pages.main_page import MainPage
from .pages.login_page import LoginPage


link1 = "http://selenium1py.pythonanywhere.com/"
link2 = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_guest_can_go_to_login_page(browser):
    link = link1
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) # Делаю инициализацию LoginPage
    login_page.should_be_login_url() # Проверяю, что мы на нужной нам странице.


def test_guest_should_see_login_link(browser):
    link = link1
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link() # выполняет метод со страницы main_page (should_be_login_link).


def test_guest_should_see_login_url(browser):
    link = link2
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    link = link2
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_should_see_register_form(browser):
    link = link2
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

