"""
Authentication UI tests.

Tests cover:
- Login with valid/invalid credentials
- Logout functionality
- User registration flows
- Account lifecycle (register -> login -> delete)
"""
import pytest
from playwright.sync_api import expect
import allure

from pages.auth_page import AuthPage
from pages.registration_page import RegistrationPage
from utils.constants import USER_DATA, SIGNUP_TEXTS


@pytest.mark.tags("ui", "regression", "smoke", "positive", "login")
@allure.feature("Authentication")
@allure.story("Login")
@allure.title("User can login with valid credentials")
def test_login_with_valid_credentials(logged_in_user: AuthPage):
    """
    Given a registered user
    When they login with valid credentials
    Then they should see their username in the header
    """
    # Assert
    expect(logged_in_user.user_account_name).to_have_text(
        f"Logged in as {USER_DATA.AVAILABLE_USER['name']}"
    )


@pytest.mark.tags("ui", "regression", "negative", "login")
@allure.feature("Authentication")
@allure.story("Login")
@allure.title("Login fails with invalid credentials")
def test_login_with_invalid_credentials(auth_page: AuthPage):
    """
    Given a user on the login page
    When they attempt to login with invalid credentials
    Then they should see an error message
    """
    # Arrange
    auth_page.navigate_to_auth_page()
    invalid_user = USER_DATA.get_new_user()
    
    # Act
    auth_page.fill_login_form(invalid_user)
    
    # Assert
    expect(auth_page.incorrect_credentials_error).to_have_text(
        SIGNUP_TEXTS.ERROR_MESSAGE_FOR_INCORRECT_CREDENTIALS
    )


@pytest.mark.tags("ui", "regression", "positive", "logout")
@allure.feature("Authentication")
@allure.story("Logout")
@allure.title("User can logout successfully")
def test_logout(logged_in_user: AuthPage):
    """
    Given a logged-in user
    When they click logout
    Then they should see the login form
    """
    # Act
    logged_in_user.click_logout_btn()
    
    # Assert
    expect(logged_in_user.login_form).to_be_visible()


@pytest.mark.parametrize("registered_user", [lambda: USER_DATA.AVAILABLE_USER], indirect=True)
@pytest.mark.tags("ui", "regression", "negative", "registration")
@allure.feature("Registration")
@allure.story("Duplicate Registration")
@allure.title("Registration fails for existing email")
def test_register_with_existing_email(auth_page: AuthPage, registered_user: dict):
    """
    Given an email that is already registered
    When a user attempts to sign up with that email
    Then they should see an error message
    """
    # Assert
    expect(auth_page.existing_email_error).to_be_visible()


@pytest.mark.parametrize("registered_user", [USER_DATA.get_new_user], indirect=True)
@pytest.mark.tags("ui", "regression", "positive", "registration", "full_registration")
@allure.feature("Registration")
@allure.story("New User Registration")
@allure.title("User can complete full registration flow")
def test_full_registration_flow(
    auth_page: AuthPage, 
    registration_page: RegistrationPage, 
    registered_user: dict
):
    """
    Given a new user with unique email
    When they complete the full registration form
    Then their account should be created
    And they should be able to delete the account
    """
    # Arrange - Verify we're on registration form
    expect(auth_page.account_info_header).to_be_visible()
    expect(registration_page.user_name).to_have_value(registered_user["name"])
    expect(registration_page.user_email).to_have_value(registered_user["email"])
    
    # Act - Complete registration
    registration_page.complete_registration(registered_user)
    
    # Assert - Account created
    expect(registration_page.account_created_msg).to_be_visible()
    
    # Cleanup - Delete account
    registration_page.click_continue_btn()
    auth_page.click_delete_account_btn()
    expect(auth_page.account_deleted_text).to_be_visible()


@pytest.mark.parametrize("registered_user", [USER_DATA.get_new_user], indirect=True)
@pytest.mark.tags("ui", "regression", "positive", "account_lifecycle")
@allure.feature("Account Management")
@allure.story("Account Lifecycle")
@allure.title("Complete account lifecycle: register, logout, login, delete")
def test_account_lifecycle(
    auth_page: AuthPage, 
    registration_page: RegistrationPage, 
    registered_user: dict
):
    """
    Given a new user
    When they register, logout, login again, and delete their account
    Then each step should complete successfully
    """
    # Register
    expect(auth_page.account_info_header).to_be_visible()
    registration_page.complete_registration(registered_user)
    expect(registration_page.account_created_msg).to_be_visible()
    
    # Logout
    registration_page.click_continue_btn()
    auth_page.click_logout_btn()
    expect(auth_page.login_form).to_be_visible()
    
    # Login with new credentials
    auth_page.fill_login_form(registered_user)
    expect(auth_page.user_account_name).to_have_text(
        f"Logged in as {registered_user['name']}"
    )
    
    # Delete account
    auth_page.click_delete_account_btn()
    expect(auth_page.account_deleted_text).to_be_visible()
