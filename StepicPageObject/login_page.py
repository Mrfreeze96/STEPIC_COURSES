from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        # Проверяем, что в текущем URL есть подстрока "login"
        assert "login" in self.browser.current_url, "Login URL is not correct"

    def should_be_login_form(self):
        # Проверяем, что на странице есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Проверяем, что на странице есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
