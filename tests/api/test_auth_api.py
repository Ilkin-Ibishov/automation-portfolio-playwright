"""
Authentication API tests.

Tests cover:
- Login verification via API
- Account registration via API
- Account lifecycle (register -> login -> delete)
"""
import pytest
import allure

from utils.api_client import APIClient
from utils.constants import USER_DATA
from utils.helper import parse_api_response


@allure.feature("API Authentication")
class TestAuthAPI:
    """API tests for authentication endpoints."""

    @pytest.mark.api
    @pytest.mark.auth
    @allure.story("Login Verification")
    @allure.title("API returns success for valid credentials")
    def test_login_with_valid_credentials(self, api_client: APIClient):
        """
        Given a registered user
        When their credentials are verified via API
        Then the response should indicate user exists
        """
        # Act
        response = api_client.verify_login(user_data=USER_DATA.AVAILABLE_USER)
        body = parse_api_response(response)
        
        # Assert
        assert body["responseCode"] == 200, f"Expected 200, got {body}"
        assert body["message"] == "User exists!", f"Unexpected message: {body}"

    @pytest.mark.api
    @pytest.mark.auth
    @allure.story("Login Verification")
    @allure.title("API returns 404 for invalid credentials")
    def test_login_with_invalid_credentials(self, api_client: APIClient):
        """
        Given non-existent user credentials
        When login is attempted via API
        Then the response should indicate user not found
        """
        # Arrange
        invalid_user = USER_DATA.get_new_user()
        
        # Act
        response = api_client.verify_login(user_data=invalid_user)
        body = parse_api_response(response)
        
        # Assert
        assert body["responseCode"] == 404, f"Expected 404, got {body}"
        assert body["message"] == "User not found!", f"Unexpected message: {body}"

    @pytest.mark.api
    @pytest.mark.auth
    @allure.story("Account Lifecycle")
    @allure.title("Complete account lifecycle via API: register, login, delete")
    def test_account_lifecycle(self, api_client: APIClient, api_account_cleanup: list):
        """
        Given a new user
        When they register, login, and delete via API
        Then each operation should succeed
        """
        # Arrange
        user_data = USER_DATA.get_new_user()
        
        # Register
        with allure.step("Register new user"):
            response, form_data = api_client.register_new_user(user_data)
            api_account_cleanup.append((form_data["email"], form_data["password"]))
            body = parse_api_response(response)
            
            assert body["responseCode"] == 201, f"Registration failed: {body}"
            assert body["message"] == "User created!", f"Unexpected message: {body}"
        
        # Login
        with allure.step("Verify login with new account"):
            response = api_client.verify_login(user_data=form_data)
            body = parse_api_response(response)
            
            assert body["responseCode"] == 200, f"Login failed: {body}"
            assert body["message"] == "User exists!", f"Unexpected message: {body}"
        
        # Delete
        with allure.step("Delete account"):
            response = api_client.delete_account(form_data["email"], form_data["password"])
            body = parse_api_response(response)
            
            assert body["responseCode"] == 200, f"Deletion failed: {body}"
            assert body["message"] == "Account deleted!", f"Unexpected message: {body}"
            
            
            # Remove from cleanup since we deleted it
            api_account_cleanup.pop()
