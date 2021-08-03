import time
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest


link_product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_into_basket(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    quiz = BasePage(browser, link)
    quiz.solve_quiz_and_get_code()
    #time.sleep(300)


def test_guest_see_product_page(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_see_product_page()


def test_guest_see_price(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    page = BasePage(browser, link)
    page.solve_quiz_and_get_code()
    page = ProductPage(browser, link)
    page.should_see_price()


def test_guest_see_message_product_is_added(browser):
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    page = BasePage(browser, link)
    page.solve_quiz_and_get_code()
    page = ProductPage(browser, link)
    page.should_see_message_product_is_added()


@pytest.mark.parametrize('qparam', ["6",pytest.param("7", marks=pytest.mark.xfail),"8","9"])
#Добавил параметрезацию с пропуском одного параметра (в котором баг)
def test_guest_can_add_product_to_basket(browser, qparam):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{qparam}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    page = BasePage(browser, link)
    page.solve_quiz_and_get_code()
    page = ProductPage(browser, link)
    page.should_see_message_product_is_added()
    page.should_see_price()
    time.sleep(0)