"""
Products API tests.

Tests cover:
- Retrieving product list via API
- Product data structure validation
"""
import pytest
import allure

from utils.api_client import APIClient
from utils.helper import parse_api_response


@pytest.mark.api
@allure.feature("Products API")
@allure.story("Product Listing")
@allure.title("API returns all products with valid structure")
def test_get_all_products(api_client: APIClient):
    """
    Given the products API endpoint
    When a GET request is made
    Then it should return a list of products with expected fields
    """
    # Act
    response = api_client.get_all_products()
    body = parse_api_response(response)
    
    # Assert - Response structure
    assert body["responseCode"] == 200, f"Expected 200, got {body}"
    assert "products" in body, f"Missing 'products' key: {list(body.keys())}"
    assert isinstance(body["products"], list), f"'products' should be list: {type(body['products'])}"
    assert len(body["products"]) > 0, "Expected at least one product"
    
    # Assert - Product structure (validate first product)
    product = body["products"][0]
    expected_fields = ["id", "name", "price", "brand", "category"]
    for field in expected_fields:
        assert field in product, f"Product missing '{field}': {product.keys()}"
