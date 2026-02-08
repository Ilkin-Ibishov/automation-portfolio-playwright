"""
Pytest configuration and shared fixtures.

Fixture Scopes:
- session: Browser instance (provided by pytest-playwright)
- function: Page, page objects, API client (test isolation)
"""
import logging
import os
import shutil
import sys
import platform
from typing import Generator

import allure
import pytest
from playwright.sync_api import Page

from pages.auth_page import AuthPage
from pages.products_page import ProductsPage
from pages.registration_page import RegistrationPage
from pages.contactus_page import ContactUsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from utils.api_client import APIClient
from utils.constants import USER_DATA


# =============================================================================
# Pytest Hooks
# =============================================================================

def pytest_runtest_setup(item):
    """Convert @pytest.mark.tags to Allure tags."""
    for marker in item.iter_markers(name="tags"):
        for tag in marker.args:
            allure.dynamic.tag(tag)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach screenshot and video to Allure on test failure."""
    outcome = yield
    report = outcome.get_result()
    
    # Store report for other fixtures to access
    setattr(item, f"rep_{report.when}", report)
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            # Attach screenshot
            try:
                allure.attach(
                    page.screenshot(),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                pass  # Silently fail if screenshot capture fails
            
            # Attach video if available
            try:
                video = page.video
                if video:
                    video_path = video.path()
                    # Video file might not be finalized yet, need to close page first
                    # But we can't close page here, so we'll attach after page closes
                    # Store path for later attachment
                    setattr(item, "_video_path", video_path)
            except Exception:
                pass


def pytest_sessionfinish(session, exitstatus):
    """Generate environment.properties for Allure report."""
    allure_dir = session.config.getoption("--alluredir")
    if not allure_dir:
        return
        
    os.makedirs(allure_dir, exist_ok=True)

    # Environment properties
    env_props = {
        "OS": platform.system(),
        "Python": sys.version.split()[0],
        "Platform": platform.machine(),
        "Base URL": "https://automationexercise.com/"
    }
    
    with open(os.path.join(allure_dir, "environment.properties"), "w") as f:
        for key, value in env_props.items():
            f.write(f"{key}={value}\n")
            
    # Copy categories.json if exists
    categories_src = os.path.join(os.path.dirname(__file__), "categories.json")
    if os.path.exists(categories_src):
        shutil.copy(categories_src, allure_dir)


# =============================================================================
# Page Object Fixtures
# =============================================================================

@pytest.fixture
def auth_page(page: Page) -> AuthPage:
    """Provide AuthPage instance."""
    return AuthPage(page)


@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    """Provide ProductsPage instance."""
    return ProductsPage(page)


@pytest.fixture
def registration_page(page: Page) -> RegistrationPage:
    """Provide RegistrationPage instance."""
    return RegistrationPage(page)


@pytest.fixture
def contact_us_page(page: Page) -> ContactUsPage:
    """Provide ContactUsPage instance."""
    return ContactUsPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    """Provide CartPage instance."""
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    """Provide CheckoutPage instance."""
    return CheckoutPage(page)


@pytest.fixture
def payment_page(page: Page) -> PaymentPage:
    """Provide PaymentPage instance."""
    return PaymentPage(page)

# =============================================================================
# UI Test Fixtures
# =============================================================================

@pytest.fixture
def logged_in_user(auth_page: AuthPage) -> AuthPage:
    """
    Navigate to auth page and log in with available test user.
    
    Returns:
        AuthPage instance with logged-in state.
    
    Note:
        Does NOT assert login success - tests own their assertions.
    """
    auth_page.navigate_to_auth_page()
    auth_page.fill_login_form(USER_DATA.AVAILABLE_USER)
    return auth_page


@pytest.fixture
def registered_user(auth_page: AuthPage, request) -> dict:
    """
    Navigate to signup and fill initial signup form.
    
    Usage:
        @pytest.mark.parametrize("registered_user", [USER_DATA.get_new_user], indirect=True)
    
    Returns:
        User data dict used for registration.
    """
    user_data = request.param() if callable(request.param) else request.param
    auth_page.navigate_to_auth_page()
    auth_page.fill_signup_form(user_data)
    return user_data


# =============================================================================
# API Test Fixtures
# =============================================================================

@pytest.fixture
def api_client(playwright) -> Generator[APIClient, None, None]:
    """Provide APIClient instance with automatic cleanup."""
    api_context = playwright.request.new_context()
    yield APIClient(api_context)
    api_context.dispose()


@pytest.fixture
def api_account_cleanup(api_client: APIClient) -> Generator[list, None, None]:
    """
    Track and cleanup API test accounts after test completion.
    
    Usage:
        def test_something(api_client, api_account_cleanup):
            response, form_data = api_client.register_new_user(user_data)
            api_account_cleanup.append((form_data['email'], form_data['password']))
    """
    created_accounts: list[tuple[str, str]] = []
    yield created_accounts
    
    for email, password in created_accounts:
        try:
            api_client.delete_account(email, password)
        except Exception:
            pass  # Best-effort cleanup


# =============================================================================
# Reporting Fixtures
# =============================================================================

@pytest.fixture(autouse=True)
def attach_logs_on_failure(caplog, request):
    """Attach captured logs to Allure on test failure."""
    with caplog.at_level(logging.INFO):
        yield
    
    # Only attach logs if test failed and logs exist
    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        if caplog.text:
            allure.attach(
                caplog.text, 
                name="Test Logs", 
                attachment_type=allure.attachment_type.TEXT
            )


@pytest.fixture(autouse=True)
def attach_video_on_failure(page: Page, request):
    """Attach video to Allure report on test failure."""
    yield
    
    # Check if test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            video = page.video
            if video:
                video_path = video.path()
                # Close video to finalize the file
                page.context.close()
                
                # Wait briefly for file to be written
                import time
                time.sleep(0.5)
                
                if os.path.exists(video_path):
                    with open(video_path, "rb") as f:
                        allure.attach(
                            f.read(),
                            name="Failure Video",
                            attachment_type=allure.attachment_type.WEBM
                        )
        except Exception:
            pass  # Silently fail if video attachment fails


# Backward compatibility aliases
login_user = logged_in_user
register_user = registered_user
cleanup_api_account = api_account_cleanup
