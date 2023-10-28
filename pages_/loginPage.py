from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages_.basePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def fill_username_field(self, username):
        userNameFieldElement = self._find_element(By.ID, "idTimestamp")
        self._fill_field(userNameFieldElement, username)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(By.ID, "_idpassword")
        self._fill_field(passwordFieldElement, password)

    def click_to_login_button(self):
        sleep(6)
        loginButtonElement = self._find_element(By.ID, "action__form_action0")
        self._click(loginButtonElement)
        sleep(6)
