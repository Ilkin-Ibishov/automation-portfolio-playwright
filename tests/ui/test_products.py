"""
Products UI tests.

Tests cover:
- Products page visibility
- Product listing functionality
"""
import pytest
from playwright.sync_api import expect
import allure

from pages.products_page import ProductsPage
from utils.constants import URLS


@pytest.mark.tags("ui", "regression", "smoke", "positive", "products")
@pytest.mark.products
@allure.feature("Products")
@allure.story("Product Listing")
@allure.title("Products page displays product list")
def test_products_page_displays_products(products_page: ProductsPage):
    """
    Given a user navigates to the products page
    When the page loads
    Then the products list should be visible
    And at least one product should be displayed
    """
    # Arrange
    products_page.navigate_to_products_page()
    
    # Assert
    expect(products_page.products_list).to_be_visible()
    assert products_page.get_products_count() > 0, "Expected at least one product"


@pytest.mark.tags("ui", "regression", "positive", "products", "search")
@pytest.mark.products_search
@allure.feature("Products")
@allure.story("Product Search")
@allure.title("User can search for products")
def test_product_search(products_page: ProductsPage):
    """
    Given a user on the products page
    When they search for a product
    Then all the products related to search are visible
    """
    # Arrange
    products_page.navigate_to_products_page()
    search_term = "top"
    
    # Act
    products_page.search_product(search_term)
    
    # Assert
    expect(products_page.searched_products_header).to_be_visible()
    assert products_page.get_products_count() > 0, "Expected search results"
    #all the products related to search are visible
    # extract all the product names and assert that they contain the search term
    product_names = products_page.product_name.all_text_contents()
    for name in product_names:
        assert search_term.lower() in name.lower(), f"Product name {name} does not contain search term {search_term}"


@pytest.mark.tags("ui", "regression", "positive", "products", "add to cart")
@pytest.mark.products_add_to_cart
@allure.feature("Products")
@allure.story("Add to Cart")
@allure.title("User can add product to cart")
def test_add_to_cart(products_page: ProductsPage):
    """
    Given a user on the products page
    When they add first product to the cart
    And click continue shopping
    And they add second product to the cart
    And click view cart
    Then they should be redirected to the cart page
    """
    # Arrange
    products_page.navigate_to_products_page()
    
    # Act
    products_page.add_product_to_cart()
    products_page.click_continue_shopping()
    products_page.add_product_to_cart(1)
    products_page.click_view_cart()
    
    # Assert
    expect(products_page.page).to_have_url(URLS.CART_URL)


