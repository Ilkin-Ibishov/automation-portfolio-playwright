import pytest
import allure
from playwright.sync_api import Page, expect

from utils.constants import URLS


@pytest.mark.ui
@pytest.mark.navigation
@allure.feature("Navigation")
@allure.story("Test Cases Page")
@allure.title("User can navigate to Test Cases page")
def test_navigation_to_test_cases_page(page: Page):
    """
    Given a user on the home page
    When they click on 'Test Cases' link in header
    Then they should be navigated to the test cases page
    """
    # Arrange
    with allure.step("Navigate to the home page"):
        page.goto(URLS.BASE_URL)

    # Act - Use header nav link specifically
    with allure.step("Click on 'Test Cases' link in header"):
        page.locator("header a[href='/test_cases']").click()

    # Assert
    with allure.step("Verify that the user is navigated to the test cases page"):
        expect(page).to_have_url("https://automationexercise.com/test_cases")
