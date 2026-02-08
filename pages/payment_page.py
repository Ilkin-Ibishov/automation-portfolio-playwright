from playwright.sync_api import Page
import allure

from pages.base_page import BasePage
from utils.constants import URLS
from locators.locators import PaymentPageLocators


class PaymentPage(BasePage):
    """Page object for payment page."""
    
    URL = URLS.PAYMENT_URL

    def __init__(self, page: Page):
        super().__init__(page)
        self.name_on_card = page.locator(PaymentPageLocators.NAME_ON_CARD)
        self.card_number = page.locator(PaymentPageLocators.CARD_NUMBER)
        self.cvc = page.locator(PaymentPageLocators.CVC)
        self.expiry_month = page.locator(PaymentPageLocators.EXPIRY_MONTH)
        self.expiry_year = page.locator(PaymentPageLocators.EXPIRY_YEAR)
        self.pay_confirm_btn = page.locator(PaymentPageLocators.PAY_CONFIRM_BTN)
        self.success_message = page.locator(PaymentPageLocators.SUCCESS_MESSAGE)
        self.order_placed_container = page.locator(PaymentPageLocators.ORDER_PLACED_CONTAINER)
        self.download_invoice_btn = page.locator(PaymentPageLocators.DOWNLOAD_INVOICE_BTN)
        self.continue_btn = page.locator(PaymentPageLocators.CONTINUE_BTN)

    @allure.step("Enter payment details")
    def enter_payment_details(self, payment_data: dict) -> None:
        """Fill in all payment card details."""
        self.name_on_card.fill(payment_data["name_on_card"])
        self.card_number.fill(payment_data["card_number"])
        self.cvc.fill(payment_data["cvc"])
        self.expiry_month.fill(payment_data["expiry_month"])
        self.expiry_year.fill(payment_data["expiry_year"])

    @allure.step("Click Pay and Confirm Order")
    def click_pay_and_confirm(self) -> None:
        """Submit payment."""
        self.pay_confirm_btn.click()

    @allure.step("Click Download Invoice")
    def click_download_invoice(self) -> None:
        """Download the order invoice."""
        self.download_invoice_btn.click()

    @allure.step("Click Continue after order")
    def click_continue(self) -> None:
        """Click continue after successful order."""
        self.continue_btn.click()
