from playwright.sync_api import Page
import allure

from pages.base_page import BasePage
from utils.constants import URLS
from locators.locators import CartPageLocators


class CartPage(BasePage):
    
    URL = URLS.CART_URL

    def __init__(self, page: Page):
        super().__init__(page)
        self.products_list = page.locator(CartPageLocators.PRODUCTS_LIST)
        self.product_items = page.locator(CartPageLocators.PRODUCT_ITEMS)
        self.product_name = page.locator(CartPageLocators.PRODUCT_NAME)
        self.product_price = page.locator(CartPageLocators.PRODUCT_PRICE)
        self.product_quantity = page.locator(CartPageLocators.PRODUCT_QUANTITY)
        self.product_total_price = page.locator(CartPageLocators.PRODUCT_TOTAL_PRICE)
        self.product_delete_btn = page.locator(CartPageLocators.PRODUCT_DELETE_BTN)
        self.checkout_btn = page.locator(CartPageLocators.CHECKOUT_BTN)

    @allure.step("Navigate to cart page")
    def navigate_to_cart_page(self) -> None:
        """Navigate to the cart page."""
        self.navigate()

    @allure.step("Get products count")
    def get_products_count(self) -> int:
        """Get the number of displayed products."""
        return self.product_items.count()

    @allure.step("Click checkout")
    def click_checkout(self) -> None:
        """Click 'Checkout' button."""
        self.checkout_btn.click()

    @allure.step("Get product name")
    def get_product_name(self, index: int = 0) -> str:
        """Get the name of a specific product."""
        return self.product_name.nth(index).text_content()

    @allure.step("Get product price")
    def get_product_price(self, index: int = 0) -> str:
        """Get the price of a specific product."""
        return self.product_price.nth(index).text_content()

    @allure.step("Get product quantity")
    def get_product_quantity(self, index: int = 0) -> str:
        """Get the quantity of a specific product."""
        return self.product_quantity.nth(index).text_content()

    @allure.step("Get product total price")
    def get_product_total_price(self, index: int = 0) -> str:
        """Get the total price of a specific product."""
        return self.product_total_price.nth(index).text_content()

    @allure.step("Click product delete button")
    def click_product_delete_button(self, index: int = 0) -> None:
        """Click the delete button for a specific product."""
        self.product_delete_btn.nth(index).click()