from playwright.sync_api import Page
import allure
from pages.base_page import BasePage
from utils.constants import URLS
from locators.locators import ProductsPageLocators


class ProductsPage(BasePage):
    
    URL = URLS.PRODUCTS_URL

    def __init__(self, page: Page):
        super().__init__(page)
        self.products_list = page.locator(ProductsPageLocators.PRODUCTS_LIST)
        self.product_items = page.locator(ProductsPageLocators.PRODUCT_ITEMS)
        self.product_name = page.locator(ProductsPageLocators.PRODUCT_NAME)
        self.product_price = page.locator(ProductsPageLocators.PRODUCT_PRICE)
        self.add_to_cart_btn = page.locator(ProductsPageLocators.ADD_TO_CART_BTN)
        self.view_product_btn = page.locator(ProductsPageLocators.VIEW_PRODUCT_BTN)
        self.search_input = page.locator(ProductsPageLocators.SEARCH_INPUT)
        self.search_btn = page.locator(ProductsPageLocators.SEARCH_BTN)
        self.searched_products_header = page.locator(ProductsPageLocators.SEARCHED_PRODUCTS_HEADER)
        self.product_detail_name = page.locator(ProductsPageLocators.PRODUCT_DETAIL_NAME)
        self.product_detail_price = page.locator(ProductsPageLocators.PRODUCT_DETAIL_PRICE)
        self.view_cart_btn = page.locator(ProductsPageLocators.VIEW_CART_BTN)
        self.added_to_cart_msg = page.locator(ProductsPageLocators.ADDED_TO_CART_MSG)
        self.continue_shopping_btn = page.locator(ProductsPageLocators.CONTINUE_SHOPPING_BTN)

    @allure.step("Navigate to products page")
    def navigate_to_products_page(self) -> None:
        """Navigate to the products listing page."""
        self.navigate()

    @allure.step("Search for product: {search_term}")
    def search_product(self, search_term: str) -> None:
        """Search for a product by name."""
        self.search_input.fill(search_term)
        self.search_btn.click()

    def get_products_count(self) -> int:
        """Get the number of displayed products."""
        return self.product_items.count()

    @allure.step("Click view product for item at index {index}")
    def click_view_product(self, index: int = 0) -> None:
        """Click 'View Product' for a specific product."""
        self.view_product_btn.nth(index).click()

    @allure.step("Add product at index {index} to cart")
    def add_product_to_cart(self, index: int = 0) -> None:
        """Add a specific product to cart."""
        self.product_items.nth(index).hover()
        self.add_to_cart_btn.nth(index).click()

    @allure.step("Click view cart")
    def click_view_cart(self) -> None:
        """Click 'View Cart' button."""
        self.view_cart_btn.click()

    @allure.step("Get product name")
    def get_product_name(self, index: int = 0) -> str:
        """Get the name of a specific product."""
        return self.product_name.nth(index).text_content()

    @allure.step("Get product price")
    def get_product_price(self, index: int = 0) -> str:
        """Get the price of a specific product."""
        return self.product_price.nth(index).text_content()

    @allure.step("Click continue shopping")
    def click_continue_shopping(self) -> None:
        """Click 'Continue Shopping' button."""
        self.continue_shopping_btn.click()

    