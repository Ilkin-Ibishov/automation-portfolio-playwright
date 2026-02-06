import pytest
from pages.contactus_page import ContactUsPage
from utils.constants import URLS
import allure
from playwright.sync_api import expect, Page

@pytest.mark.tags("ui", "regression", "positive", "contact")
@pytest.mark.contact
@allure.feature("Contact Us")
@allure.story("Contact Us")
@allure.title("User can contact us successfully")
def test_contact_us(page: Page, contact_us_page: ContactUsPage):
    """
    Given a user on the contact us page
    When they fill out the contact form
    And click submit
    Then they should see a success message
    """
    # Arrange
    contact_us_page.navigate_to_contact_us_page()
    
    # Act
    page.on("dialog", lambda dialog: dialog.accept())
    contact_us_page.fill_contact_us_form()
    
    # Assert
    expect(contact_us_page.success_message).to_be_visible()
    #teardown
    contact_us_page.delete_test_file()

    
