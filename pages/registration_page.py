"""
Registration page object for account creation workflow.
"""
from playwright.sync_api import Page
import allure

from pages.base_page import BasePage
from locators.locators import RegistrationPageLocators
from utils.constants import ADDRESS_DATA


class RegistrationPage(BasePage):
    """Page object for account information form during registration."""

    def __init__(self, page: Page):
        super().__init__(page)
        # Account info
        self.user_name = page.locator(RegistrationPageLocators.USER_NAME)
        self.user_email = page.locator(RegistrationPageLocators.USER_EMAIL)
        self.title_mr = page.locator(RegistrationPageLocators.TITLE_MR)
        self.title_mrs = page.locator(RegistrationPageLocators.TITLE_MRS)
        self.password = page.locator(RegistrationPageLocators.PASSWORD)
        self.day = page.locator(RegistrationPageLocators.DAY)
        self.month = page.locator(RegistrationPageLocators.MONTH)
        self.year = page.locator(RegistrationPageLocators.YEAR)
        self.newsletter = page.locator(RegistrationPageLocators.NEWSLETTER)
        self.offers = page.locator(RegistrationPageLocators.OFFERS)
        
        # Address info
        self.first_name = page.locator(RegistrationPageLocators.FIRST_NAME)
        self.last_name = page.locator(RegistrationPageLocators.LAST_NAME)
        self.company = page.locator(RegistrationPageLocators.COMPANY)
        self.address1 = page.locator(RegistrationPageLocators.ADDRESS)
        self.address2 = page.locator(RegistrationPageLocators.ADDRESS2)
        self.country = page.locator(RegistrationPageLocators.COUNTRY)
        self.state = page.locator(RegistrationPageLocators.STATE)
        self.city = page.locator(RegistrationPageLocators.CITY)
        self.zipcode = page.locator(RegistrationPageLocators.ZIPCODE)
        self.mobile_number = page.locator(RegistrationPageLocators.MOBILE_NUMBER)
        
        # Actions
        self.create_account_btn = page.locator(RegistrationPageLocators.CREATE_ACCOUNT_BTN)
        self.continue_btn = page.locator(RegistrationPageLocators.CONTINUE_BTN)
        self.account_created_msg = page.locator(RegistrationPageLocators.ACCOUNT_CREATED_SUCCESS)

    @allure.step("Fill account details")
    def fill_account_details(self, user_data: dict) -> None:
        """
        Fill account information section.
        
        Args:
            user_data: Dict with 'password', 'day', 'month', 'year' keys.
        """
        self.title_mr.check()
        self.password.fill(user_data["password"])
        self.day.select_option(user_data["day"])
        self.month.select_option(user_data["month"])
        self.year.select_option(user_data["year"])
        self.newsletter.check()
        self.offers.check()

    @allure.step("Fill address details")
    def fill_address_details(self, address_data: dict = None) -> None:
        """
        Fill address information section.
        
        Args:
            address_data: Optional dict with address fields. 
                         Uses ADDRESS_DATA.DEFAULT if not provided.
        """
        data = address_data or ADDRESS_DATA.DEFAULT
        self.first_name.fill(data["first_name"])
        self.last_name.fill(data["last_name"])
        self.company.fill(data["company"])
        self.address1.fill(data["address"])
        self.address2.fill(data["address2"])
        self.country.select_option(data["country"])
        self.state.fill(data["state"])
        self.city.fill(data["city"])
        self.zipcode.fill(data["zipcode"])
        self.mobile_number.fill(data["phone"])

    @allure.step("Click Create Account button")
    def click_create_account_btn(self) -> None:
        """Submit the registration form."""
        self.create_account_btn.click()

    @allure.step("Click Continue button")
    def click_continue_btn(self) -> None:
        """Click continue after account creation."""
        self.continue_btn.click()

    def complete_registration(self, user_data: dict, address_data: dict = None) -> None:
        """
        Complete full registration form in one step.
        
        Args:
            user_data: User account data.
            address_data: Optional address data.
        """
        self.fill_account_details(user_data)
        self.fill_address_details(address_data)
        self.click_create_account_btn()
