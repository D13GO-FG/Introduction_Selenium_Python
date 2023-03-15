import pytest

from pageObjects.WebFormPage import WebFormPage


class TestWebForm:

    @pytest.mark.parametrize('text', ['python', 'java', 'c#'])
    def test_web_form(self, setup, text):
        self.driver = setup
        # Given the Web Form page is displayed
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")
        web_form_page = WebFormPage(self.driver)
        # When the user type the inputs
        web_form_page.set_text_input(text)
        web_form_page.set_text_password(text)
        web_form_page.set_text_area(text)
        # Then the user click submit
        # And the page change to "form submitted"
        # And the page shows Received!
