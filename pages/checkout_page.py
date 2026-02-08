from playwright.sync_api import Page
import allure

from pages.base_page import BasePage
from utils.constants import URLS
from locators.locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    """Page object for checkout/order review page."""
    
    URL = URLS.CHECKOUT_URL

    def __init__(self, page: Page):
        super().__init__(page)
        self.delivery_address = page.locator(CheckoutPageLocators.DELIVERY_ADDRESS)
        self.billing_address = page.locator(CheckoutPageLocators.BILLING_ADDRESS)
        self.cart_items = page.locator(CheckoutPageLocators.CART_ITEMS)
        self.comment_textarea = page.locator(CheckoutPageLocators.COMMENT_TEXTAREA)
        self.place_order_btn = page.locator(CheckoutPageLocators.PLACE_ORDER_BTN)
        self.register_login_btn = page.locator(CheckoutPageLocators.REGISTER_LOGIN_BTN)

    @allure.step("Enter order comment")
    def enter_comment(self, comment: str) -> None:
        """Enter a comment for the order."""
        self.comment_textarea.fill(comment)

    @allure.step("Click Place Order")
    def click_place_order(self) -> None:
        """Click the Place Order button to proceed to payment."""
        self.place_order_btn.click()

    @allure.step("Click Register/Login from checkout modal")
    def click_register_login(self) -> None:
        """Click Register/Login when prompted during checkout."""
        self.register_login_btn.click()

    def get_delivery_address_text(self) -> str:
        """Get the delivery address text."""
        return self.delivery_address.text_content()

    def get_billing_address_text(self) -> str:
        """Get the billing address text."""
        return self.billing_address.text_content()

    def get_cart_items_count(self) -> int:
        """Get the number of items in the cart summary."""
        return self.cart_items.count()
