from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    PHONE_INPUT = (By.XPATH, "//input[@type='tel']")
    CONTINUE_BTN = (By.CLASS_NAME, "submitBottomOption")
    ERROR_NOTIF = (By.CLASS_NAME, "notify-error")
    OTP_CONTAINER = (By.CLASS_NAME, "otpContainer")

    def enter_mobile_number(self, number):
        self.type_text(self.PHONE_INPUT, number)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def is_error_displayed(self):
        errors = self.driver.find_elements(*self.ERROR_NOTIF)
        return len(errors) > 0 and errors[0].is_displayed()

    def is_otp_screen_visible(self):
        return self.find(self.OTP_CONTAINER).is_displayed()