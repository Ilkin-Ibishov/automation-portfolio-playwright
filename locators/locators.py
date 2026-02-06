class CommonLocators:
    """Shared locators used across multiple pages."""
    USER_ACCOUNT_NAME = "a:has-text('Logged in as')"
    LOGOUT_BTN = "a[href='/logout']"


class HomePageLocators:
    """Locators for the home page."""
    SIGNUP_LOGIN_BTN = "a[href='/login']"
    HOME_SLIDER = "#slider-carousel"


class AuthPageLocators:
    """Locators for login and signup forms."""
    LOGIN_FORM = ".login-form"
    SIGNUP_FORM = ".signup-form"
    LOGIN_EMAIL_INPUT = "[data-qa='login-email']"
    LOGIN_PASSWORD_INPUT = "[data-qa='login-password']"
    LOGIN_BTN = "[data-qa='login-button']"
    SIGNUP_NAME_INPUT = "[data-qa='signup-name']"
    SIGNUP_EMAIL_INPUT = "[data-qa='signup-email']"
    SIGNUP_BTN = "[data-qa='signup-button']"
    INCORRECT_CREDENTIALS_ERROR = "form[action='/login'] p"
    DELETE_ACCOUNT_BTN = "a[href='/delete_account']"
    ACCOUNT_DELETED_TEXT = "[data-qa='account-deleted']"
    ACCOUNT_DELETED_CONTINUE = "[data-qa='continue-button']"


class RegistrationPageLocators:
    """Locators for user account registration form."""
    USER_NAME = "[data-qa='name']"
    USER_EMAIL = "[data-qa='email']"
    TITLE_MR = "#id_gender1"
    TITLE_MRS = "#id_gender2"
    PASSWORD = "[data-qa='password']"
    DAY = "[data-qa='days']"
    MONTH = "[data-qa='months']"
    YEAR = "[data-qa='years']"
    NEWSLETTER = "#newsletter"
    OFFERS = "#optin"
    FIRST_NAME = "[data-qa='first_name']"
    LAST_NAME = "[data-qa='last_name']"
    COMPANY = "[data-qa='company']"
    ADDRESS = "[data-qa='address']"
    ADDRESS2 = "[data-qa='address2']"
    COUNTRY = "[data-qa='country']"
    STATE = "[data-qa='state']"
    CITY = "[data-qa='city']"
    ZIPCODE = "[data-qa='zipcode']"
    MOBILE_NUMBER = "[data-qa='mobile_number']"
    CREATE_ACCOUNT_BTN = "[data-qa='create-account']"
    CONTINUE_BTN = "[data-qa='continue-button']"
    ACCOUNT_CREATED_SUCCESS = "h2:has-text('Account Created!')"


class ProductsPageLocators:
    """Locators for products listing and search functionality."""
    ALL_PRODUCTS_HEADER = "h2.title.text-center"
    PRODUCTS_LIST = ".features_items"
    PRODUCT_ITEMS = ".features_items .product-image-wrapper"
    PRODUCT_NAME = ".productinfo p"
    PRODUCT_PRICE = ".productinfo h2"
    ADD_TO_CART_BTN = ".overlay-content .add-to-cart"
    VIEW_PRODUCT_BTN = ".choose a"
    SEARCH_INPUT = "#search_product"
    SEARCH_BTN = "#submit_search"
    SEARCHED_PRODUCTS_HEADER = "h2.title.text-center:has-text('Searched Products')"
    PRODUCT_DETAIL_NAME = ".product-information h2"
    PRODUCT_DETAIL_PRICE = ".product-information span span"
    VIEW_CART_BTN = ".modal-body p a[href='/view_cart']"
    ADDED_TO_CART_MSG = ".modal-body p:has-text('Your product has been added to cart.')"
    CONTINUE_SHOPPING_BTN = ".modal-footer button.btn-success"

class CartPageLocators:
    PRODUCTS_LIST = "tbody"
    PRODUCT_ITEMS = "tr"
    PRODUCT_NAME = "td.cart_description h4 a"
    PRODUCT_PRICE = "td.cart_price p"
    PRODUCT_QUANTITY = "td.cart_quantity button.disabled"
    PRODUCT_TOTAL_PRICE = "td.cart_total p.cart_total_price"
    PRODUCT_DELETE_BTN = "td.cart_delete a.cart_quantity_delete"
    CHECKOUT_BTN = ".check_out"


class ContactUsPageLocators:
    GET_IN_TOUCH_HEADER = "h2.title.text-center"
    CONTACT_US_FORM = "form[action='/contact_us']"
    NAME_INPUT = "[data-qa='name']"
    EMAIL_INPUT = "[data-qa='email']"
    SUBJECT_INPUT = "[data-qa='subject']"
    MESSAGE_INPUT = "[data-qa='message']"
    FILE_INPUT = "input[name='upload_file']"
    SUBMIT_BTN = "[data-qa='submit-button']"
    SUCCESS_MESSAGE = ".contact-form .alert-success"
    
    
