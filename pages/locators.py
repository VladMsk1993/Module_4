from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #Добавили кортеж из двух значений.


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRICE = (By.XPATH, "//strong[text() = '£9.99']")
    PRODUCT = (By.XPATH, "//strong[text() = \"The shellcoder's handbook\"]")
