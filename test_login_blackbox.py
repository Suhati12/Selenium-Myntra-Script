import time
import pytest
from config.config import Config
from pages.login_page import LoginPage

class TestLoginBlackBox:

    def test_bva_invalid_short_mobile(self, driver):
        """BVA: Test phone number under 10 digits (9 digits)."""
        login_page = LoginPage(driver)
        login_page.open_url(Config.LOGIN_URL)
        
        login_page.enter_mobile_number("987654321")
        login_page.click_continue()
        
        time.sleep(1)
        login_page.take_screenshot("bva_failure_check")
        
        # Verify validation error or form blocking
        assert login_page.is_error_displayed() or driver.current_url == Config.LOGIN_URL

    def test_ep_valid_mobile(self, driver):
        """EP: Test valid 10-digit mobile number input."""
        login_page = LoginPage(driver)
        login_page.open_url(Config.LOGIN_URL)
        
        login_page.enter_mobile_number("9876543210")
        login_page.click_continue()
        
        assert login_page.is_otp_screen_visible()