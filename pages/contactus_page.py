from playwright.sync_api import Page
import allure

from pages.base_page import BasePage
from utils.constants import URLS
from locators.locators import ContactUsPageLocators

class ContactUsPage(BasePage):
    
    URL = URLS.CONTACT_US_URL

    def __init__(self, page: Page):
        super().__init__(page)
        self.get_in_touch_header = page.locator(ContactUsPageLocators.GET_IN_TOUCH_HEADER)
        self.contact_us_form = page.locator(ContactUsPageLocators.CONTACT_US_FORM)
        self.name_input = page.locator(ContactUsPageLocators.NAME_INPUT)
        self.email_input = page.locator(ContactUsPageLocators.EMAIL_INPUT)
        self.subject_input = page.locator(ContactUsPageLocators.SUBJECT_INPUT)
        self.message_input = page.locator(ContactUsPageLocators.MESSAGE_INPUT)
        self.file_input = page.locator(ContactUsPageLocators.FILE_INPUT)
        self.submit_btn = page.locator(ContactUsPageLocators.SUBMIT_BTN)
        self.success_message = page.locator(ContactUsPageLocators.SUCCESS_MESSAGE)

    @allure.step("Navigate to contact us page")
    def navigate_to_contact_us_page(self) -> None:
        """Navigate to the contact us page."""
        self.navigate()

    @allure.step("Fill contact us form")
    def fill_contact_us_form(self) -> None:
        """Fill the contact us form with user data."""
        self.name_input.fill("John Doe")
        self.email_input.fill("john.doe@example.com")
        self.subject_input.fill("Test Subject")
        self.message_input.fill("This is a test message.")
        with open("demo.txt", "w") as f:
            f.write("This is a test file for upload.")
        self.file_input.set_input_files("demo.txt")
        self.submit_btn.click()

    @allure.step("Verify success message")
    def verify_success_message(self) -> None:
        """Verify that the success message is displayed."""
        self.success_message.wait_for(state="visible")

    #Delete test file
    @allure.step("Delete test file")
    def delete_test_file(self):
        try:
            os.remove("demo.txt")
        except FileNotFoundError:
            pass