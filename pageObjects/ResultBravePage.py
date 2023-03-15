from selenium.webdriver.common.by import By


class ResultBing:
    # Initializer
    def __init__(self, driver):
        self.driver = driver

    # Locators
    SEARCH_INPUT = (By.ID, "searchbox")
    RESULT_LINKS = (By.CLASS_NAME, "snippet-title")

    # Interaction Methods
    def result_link_titles(self):
        links = self.driver.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.driver.title
