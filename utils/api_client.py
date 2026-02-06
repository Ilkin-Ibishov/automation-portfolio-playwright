"""
API client for automationexercise.com API interactions.

This module provides a clean interface for API operations.
Assertions are NOT included here - tests own their assertions.
"""
from playwright.sync_api import APIRequestContext, APIResponse
import allure

from utils.constants import URLS, ADDRESS_DATA


class APIClient:
    """Client for making API requests to Automation Exercise."""
    
    BASE_URL = URLS.API_BASE_URL

    def __init__(self, request: APIRequestContext):
        self.request = request

    @allure.step("POST /createAccount - Register new user")
    def register_new_user(self, user_data: dict) -> tuple[APIResponse, dict]:
        """
        Register a new user via the API.
        
        Args:
            user_data: Dict with keys: name, email, password, day, month, year.
        
        Returns:
            Tuple of (response, form_data) where form_data includes all submitted fields.
        
        Raises:
            ValueError: If required user_data keys are missing.
        """
        required_keys = ["email", "password", "name", "day", "month", "year"]
        missing = [k for k in required_keys if k not in user_data]
        if missing:
            raise ValueError(f"user_data missing required keys: {missing}")
        
        address = ADDRESS_DATA.DEFAULT
        form_data = {
            "name": user_data["name"],
            "email": user_data["email"],
            "password": user_data["password"],
            "title": "Mr",
            "birth_date": user_data["day"],
            "birth_month": user_data["month"],
            "birth_year": user_data["year"],
            "firstname": address["first_name"],
            "lastname": address["last_name"],
            "company": address["company"],
            "address1": address["address"],
            "address2": address["address2"],
            "country": address["country"],
            "zipcode": address["zipcode"],
            "state": address["state"],
            "city": address["city"],
            "mobile_number": address["phone"],
        }
        
        response = self.request.post(f"{self.BASE_URL}/createAccount", form=form_data)
        return response, form_data

    @allure.step("DELETE /deleteAccount - Delete user account")
    def delete_account(self, email: str, password: str) -> APIResponse:
        """
        Delete a user account via the API.
        
        Args:
            email: User's email address.
            password: User's password.
        
        Returns:
            API response object.
        """
        form_data = {"email": email, "password": password}
        return self.request.delete(f"{self.BASE_URL}/deleteAccount", form=form_data)
    
    @allure.step("POST /verifyLogin - Verify user credentials")
    def verify_login(self, user_data: dict) -> APIResponse:
        """
        Verify user login credentials via the API.
        
        Args:
            user_data: Dict with keys: email, password.
        
        Returns:
            API response object.
        """
        form_data = {"email": user_data["email"], "password": user_data["password"]}
        return self.request.post(f"{self.BASE_URL}/verifyLogin", form=form_data)

    @allure.step("GET /productsList - Retrieve all products")
    def get_all_products(self) -> APIResponse:
        """
        Get all products from the API.
        
        Returns:
            API response object.
        """
        return self.request.get(f"{self.BASE_URL}/productsList")