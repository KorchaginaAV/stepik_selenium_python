from .BasePage import BasePage
from .Locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert (
            current_url.find("login") != -1
        ), f'Текущий url "{current_url}", а не страница логина'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "На странице нет формы логина"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "На странице нет формы регистрации"

    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL
        )
        registration_email.send_keys(email)
        registration_password1 = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD1
        )
        registration_password1.send_keys(password)
        registration_password2 = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD2
        )
        registration_password2.send_keys(password)
        registration_button = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_BUTTON
        )
        registration_button.submit()
