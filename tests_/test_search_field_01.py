from selenium import webdriver
import unittest
from pages_.navigationBar import NavigationBar
from pages_.searchResultPage import SearchResultPage
from time import sleep

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("https://www.list.am")

    def test_search_functionality(self):
        NavigationBarObj = NavigationBar(self.driver)
        NavigationBarObj.fill_search_field("cars")
        NavigationBarObj.click_to_search_icon()
        sleep(10)

    def test_search_first_product_select(self):
        SearchResultObj = SearchResultPage(self.driver)
        SearchResultObj.click_to_first_product()

    def tearDown(self):
        self.driver.close()
