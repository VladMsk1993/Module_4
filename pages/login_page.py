from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "There's not the substring"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        except():
            assert self.browser.is_element_present(*LoginPageLocators.LOGIN_FORM), "There's not login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        except():
            assert self.browser.is_element_present(*LoginPageLocators.REGISTER_FORM), "There's not register form"
