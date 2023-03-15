from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class SearchBing:
    # URL
    URL = "https://www.bing.com/"

    # Locators
    SEARCH_INPUT = (By.ID, "sb_form_q")

    # Initializer
    def __init__(self, driver):
        self.driver = driver

    # Interaction Methods
    def load(self):
        self.driver.get(self.URL)

    def search(self, phrase):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
