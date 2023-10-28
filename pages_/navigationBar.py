from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class NavigationBar(BasePage):

    def fill_search_field(self, text):
        searchFieldElement = self._find_element(By.ID, "idSearchBox")
        self._fill_field(searchFieldElement, text)

    def click_to_search_icon(self):
        searchIconElement = self._find_element(By.XPATH, "//button[@type='button']")
        self._click(searchIconElement)