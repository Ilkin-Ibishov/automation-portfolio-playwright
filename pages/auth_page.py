from playwright.sync_api import Page
import allure

from pages.base_page import BasePage
from utils.constants import URLS
from locators.locators import AuthPageLocators, CommonLocators


class AuthPage(BasePage):
    """Page object for /login page handling login and signup forms."""
    
    URL = URLS.BASE_URL + "login"

    def __init__(self, page: Page):
        super().__init__(page)
        # Login form
        self.login_form = page.locator(AuthPageLocators.LOGIN_FORM)
        self.login_email_input = page.locator(AuthPageLocators.LOGIN_EMAIL_INPUT)
        self.login_password_input = page.locator(AuthPageLocators.LOGIN_PASSWORD_INPUT)
        self.login_btn = page.locator(AuthPageLocators.LOGIN_BTN)
        
        # Signup form
        self.signup_form = page.locator(AuthPageLocators.SIGNUP_FORM)
        self.signup_name_input = page.locator(AuthPageLocators.SIGNUP_NAME_INPUT)
        self.signup_email_input = page.locator(AuthPageLocators.SIGNUP_EMAIL_INPUT)
        self.signup_btn = page.locator(AuthPageLocators.SIGNUP_BTN)
        
        # Shared elements
        self.user_account_name = page.locator(CommonLocators.USER_ACCOUNT_NAME)
        self.logout_btn = page.locator(CommonLocators.LOGOUT_BTN)
        
        # Error messages
        self.incorrect_credentials_error = page.locator(AuthPageLocators.INCORRECT_CREDENTIALS_ERROR)
        self.existing_email_error = page.get_by_text("Email Address already exist!")
        
        # Account management
        self.delete_account_btn = page.locator(AuthPageLocators.DELETE_ACCOUNT_BTN)
        self.account_deleted_text = page.locator(AuthPageLocators.ACCOUNT_DELETED_TEXT)
        self.account_deleted_continue = page.locator(AuthPageLocators.ACCOUNT_DELETED_CONTINUE)
        
        # Registration flow
        self.account_info_header = page.get_by_text("Enter Account Information")

    @allure.step("Navigate to login/signup page")
    def navigate_to_auth_page(self) -> None:
        """Navigate to the authentication page."""
        self.navigate()

    @allure.step("Fill login form and submit")
    def fill_login_form(self, user_data: dict) -> None:
        """Fill email/password and click login."""
        self.login_email_input.fill(user_data["email"])
        self.login_password_input.fill(user_data["password"])
        self.login_btn.click()

    @allure.step("Fill signup form and submit")
    def fill_signup_form(self, user_data: dict) -> None:
        """Fill name/email and click signup."""
        self.signup_name_input.fill(user_data["name"])
        self.signup_email_input.fill(user_data["email"])
        self.signup_btn.click()

    @allure.step("Click logout")
    def click_logout_btn(self) -> None:
        """Click the logout button."""
        self.logout_btn.click()

    @allure.step("Click delete account")
    def click_delete_account_btn(self) -> None:
        """Click the delete account button."""
        self.delete_account_btn.click()
