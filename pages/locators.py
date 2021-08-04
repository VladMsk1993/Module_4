from selenium.webdriver.common.by import By


#class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRICE = (By.XPATH, "//*[@id=\"content_inner\"]/article/div[1]/div[2]/p[1]")
    BASKET_PRICE = (By.XPATH, "// *[@id =\"messages\"]/div[3]/div/p[1]/strong")
    PRODUCT = (By.XPATH, "//strong[text()=\"The shellcoder's handbook\"]")
    MESSAGE_PRODUCT = (By.XPATH, "//*[@id=\"messages\"]/div[1]/div/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id=\"messages\"]/div[1]/div")
    PRODUCT = (By.XPATH, "//*[@id=\"content_inner\"]/article/div[1]/div[2]/h1")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # Добавили кортеж из двух значений.