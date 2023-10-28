from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages_.basePage import BasePage


class LoginPage(BasePage):

    def fill_username_field(self, username):
        userNameFieldElement = self._find_element(By.ID, "_idphone_number_or_email")
        self._fill_field(userNameFieldElement, username)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(By.ID, "_idpassword")
        self._fill_field(passwordFieldElement, password)

    def click_to_login_button(self):
        loginButtonElement = self._find_element(By.ID, "action__form_action0")
        self._click(loginButtonElement)

