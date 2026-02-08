from utils.helper import get_unique_email


class URLS:
    """Application URLs."""
    BASE_URL = "https://automationexercise.com/"
    API_BASE_URL = "https://automationexercise.com/api"
    PRODUCTS_URL = "https://automationexercise.com/products"
    CART_URL = "https://automationexercise.com/view_cart"
    CHECKOUT_URL = "https://automationexercise.com/checkout"
    PAYMENT_URL = "https://automationexercise.com/payment"
    CONTACT_US_URL = "https://automationexercise.com/contact_us"


class USER_DATA:
    """Test user data with clear lifecycle and consistent structure."""
    
    AVAILABLE_USER = {
        "name": "ilkin test002",
        "email": "ilkin.test002@gmail.com",
        "password": "test002",
        "day": "15",
        "month": "May",
        "year": "1990"
    }

    @staticmethod
    def get_new_user() -> dict:
        """
        Generate a unique test user with dynamic email.
        Safe for parallel test execution.
        """
        return {
            "name": "testuser",
            "email": get_unique_email(),
            "password": "NewPassword123",
            "day": "15",
            "month": "May",
            "year": "1990"
        }


class SIGNUP_TEXTS:
    """Expected UI text messages for signup/authentication workflows."""
    
    ACCOUNT_INFO_PAGE_HEADER = "Enter Account Information"
    LOGIN_PAGE_TITLE = "Automation Exercise - Signup / Login"
    ERROR_MESSAGE_FOR_EXISTING_USER = "Email Address already exist!"
    ERROR_MESSAGE_FOR_INCORRECT_CREDENTIALS = "Your email or password is incorrect!"


class ADDRESS_DATA:
    """Predefined test data for address and account information forms."""
    
    DEFAULT = {
        "first_name": "John",
        "last_name": "Doe",
        "company": "Test Company",
        "address": "123 Test Street",
        "address2": "Suite 100",
        "country": "United States",
        "state": "California",
        "city": "San Francisco",
        "zipcode": "94105",
        "phone": "+1-555-123-4567",
    }


class PAYMENT_DATA:
    """Test payment card data."""
    
    DEFAULT = {
        "name_on_card": "John Doe",
        "card_number": "4111111111111111",
        "cvc": "123",
        "expiry_month": "12",
        "expiry_year": "2025",
    }


# Backward compatibility alias
class ACCOUNT_INFO_PAGE_TEXTS:
    """Deprecated: Use ADDRESS_DATA instead."""
    ADDRESS_DATA = ADDRESS_DATA.DEFAULT
