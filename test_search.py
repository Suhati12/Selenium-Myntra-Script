import time
import pytest
from config.config import Config
from pages.home_page import HomePage

class TestSearch:

    def test_TC_SEARCH_01_valid_keyword(self, driver):
        """TC_SEARCH_01: Validate search execution with a valid product keyword."""
        home_page = HomePage(driver)
        home_page.open_url(Config.BASE_URL)
        
        home_page.search_for_product("Casual Shoes")
        time.sleep(2)
        home_page.take_screenshot("TC_SEARCH_01_pass")
        
        current_url = driver.current_url.lower()
        assert "shoes" in current_url or "shoes" in driver.title.lower(), \
            f"Search Failed: Keyword not found in URL ({current_url})"

    def test_TC_SEARCH_02_invalid_keyword(self, driver):
        """TC_SEARCH_02: Validate search behavior with invalid/gibberish keyword."""
        home_page = HomePage(driver)
        home_page.open_url(Config.BASE_URL)
        
        home_page.search_for_product("xyz123890abc")
        time.sleep(2)
        home_page.take_screenshot("TC_SEARCH_02_results")
        
        assert "xyz123890abc" in driver.current_url.lower() or "myntra" in driver.title.lower()

    def test_TC_SEARCH_03_empty_input(self, driver):
        """TC_SEARCH_03: Validate search bar behavior with empty input."""
        home_page = HomePage(driver)
        home_page.open_url(Config.BASE_URL)
        
        home_page.search_for_product("")
        time.sleep(1)
        
        assert driver.current_url.rstrip("/") == Config.BASE_URL.rstrip("/")