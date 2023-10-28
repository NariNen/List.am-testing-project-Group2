from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):

    def click_to_first_product(self):
        firstProductElement = self._find_element(By.XPATH, "(//a[@target='_blank'])[2]")
        self._click(firstProductElement)