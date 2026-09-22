from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BAR = (By.CLASS_NAME, "desktop-searchBar")

    def search_for_product(self, product_name):
        self.type_text(self.SEARCH_BAR, product_name)
        self.find(self.SEARCH_BAR).send_keys(Keys.ENTER)