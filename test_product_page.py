import time

from .pages.product_page import ProductPage
from .pages.base_page import BasePage


link_basket = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_into_basket(browser):
    link = link_basket
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    quiz = BasePage(browser, link)
    quiz.solve_quiz_and_get_code()
    time.sleep(2)


def test_guest_see_product_page(browser):
    link = link_basket
    page = ProductPage(browser, link)
    page.open()
    page.should_see_product_page()


def test_guest_see_price(browser):
    link = link_basket
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    quiz = BasePage(browser, link)
    quiz.solve_quiz_and_get_code()
    page.should_see_price()


def test_guest_see_message_product_is_added(browser):
    link = link_basket
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add_to_basket()
    quiz = BasePage(browser, link)
    quiz.solve_quiz_and_get_code()
    page.should_see_message_product_is_added()







