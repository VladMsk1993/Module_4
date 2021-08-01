from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        check_url = self.browser.current_url
        # реализуйте проверку на корректный url адрес
        assert "login" in check_url, "There's not the substring"

    def should_be_login_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
            # реализуйте проверку, что есть форма логина
        except():
            assert self.browser.is_element_present(*LoginPageLocators.LOGIN_FORM), "There's not login form"

    def should_be_register_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
            # реализуйте проверку, что есть форма регистрации на странице
        except():
            assert self.browser.is_element_present(*LoginPageLocators.REGISTER_FORM), "There's not register form"
