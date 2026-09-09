from playwright.sync_api import Page
import allure
from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(
            page,
            locator="login-form-email-input",
            name="Email"
        )

        self.password_input = Input(
            page,
            locator="login-form-password-input",
            name="Password"
        )
    @allure.step("Fill login form")

    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)