from selenium import webdriver
from selenium.webdriver.common.by import By

class NavigationBar():
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        pass

    def search_field(self, text):
        searchFieldElement = self.driver.find_element(By.ID, "idSearchBox")
        searchFieldElement.send_keys()

    def click_to_search_icon(self):
        searchIconElement = self.driver.find_element(By.XPATH, "//button[@type='button']")
        searchIconElement.click()