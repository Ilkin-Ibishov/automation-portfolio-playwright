"""
Checkout flow UI tests (TC 14-16, 23, 24).

Tests cover:
- Place order with registration during checkout
- Place order with pre-registration
- Place order as logged-in user
"""
import pytest
from playwright.sync_api import expect
import allure

from pages.auth_page import AuthPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.registration_page import RegistrationPage
from utils.constants import USER_DATA, PAYMENT_DATA


@pytest.mark.ui
@pytest.mark.checkout
@allure.feature("Checkout")
@allure.story("Login Before Checkout")
@allure.title("TC16: Place order after login")
def test_place_order_login_before_checkout(
    logged_in_user: AuthPage,
    products_page: ProductsPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
    payment_page: PaymentPage
):
    """
    Given a logged-in user
    When they add products, proceed to checkout, and complete payment
    Then the order should be placed successfully
    """
    # Add product to cart
    products_page.navigate_to_products_page()
    products_page.add_product_to_cart()
    products_page.click_view_cart()
    expect(cart_page.product_items.first).to_be_visible()
    
    # Proceed to checkout
    cart_page.click_checkout()
    expect(checkout_page.delivery_address).to_be_visible()
    
    # Place order
    checkout_page.enter_comment("Please deliver between 9am-5pm")
    checkout_page.click_place_order()
    
    # Complete payment
    payment_page.enter_payment_details(PAYMENT_DATA.DEFAULT)
    payment_page.click_pay_and_confirm()
    
    # Assert order success
    expect(payment_page.order_placed_container).to_be_visible()


@pytest.mark.parametrize("registered_user", [USER_DATA.get_new_user], indirect=True)
@pytest.mark.ui
@pytest.mark.checkout
@allure.feature("Checkout")
@allure.story("Register Before Checkout")
@allure.title("TC15: Place order after registration")
def test_place_order_register_before_checkout(
    auth_page: AuthPage,
    registration_page: RegistrationPage,
    products_page: ProductsPage,
    cart_page: CartPage,
    checkout_page: CheckoutPage,
    payment_page: PaymentPage,
    registered_user: dict
):
    """
    Given a new user who just registered
    When they add products and complete checkout
    Then the order should be placed successfully
    And the account should be cleaned up
    """
    # Complete registration
    expect(auth_page.account_info_header).to_be_visible()
    registration_page.complete_registration(registered_user)
    expect(registration_page.account_created_msg).to_be_visible()
    registration_page.click_continue_btn()
    
    # Add product to cart
    products_page.navigate_to_products_page()
    products_page.add_product_to_cart()
    products_page.click_view_cart()
    expect(cart_page.product_items.first).to_be_visible()
    
    # Proceed to checkout
    cart_page.click_checkout()
    expect(checkout_page.delivery_address).to_be_visible()
    
    # Place order
    checkout_page.enter_comment("Test order")
    checkout_page.click_place_order()
    
    # Complete payment
    payment_page.enter_payment_details(PAYMENT_DATA.DEFAULT)
    payment_page.click_pay_and_confirm()
    
    # Assert order success
    expect(payment_page.order_placed_container).to_be_visible()
    
    # Cleanup - delete account
    payment_page.click_continue()
    auth_page.click_delete_account_btn()
    expect(auth_page.account_deleted_text).to_be_visible()
