import time

from pages_.loginPage import LoginPage
from selenium import webdriver
import unittest
from time import sleep


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("https://www.list.am/login")

    def test_login_in_positive_test(self):
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("lilmankan@gmail.com")
        loginPageObj.fill_password_field("1234567*")
        time.sleep(8)
        # to avoid captcha check
        loginPageObj.click_to_login_button()

    def test_login_in_negative_test(self):
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("lilmankan@gmail.com")
        loginPageObj.fill_password_field("1kjghlirughl")
        time.sleep(8)
        loginPageObj.click_to_login_button()
        print("Error: Incorrect password")

    def tearDown(self):
        self.driver.close()