from seleniumpagefactory import PageFactory


class WebFormPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'text_input': ('ID', "my-text-id"),
        'password': ('NAME', "my-password"),
        'text_area': ('NAME', "my-textarea")
    }

    def set_text_input(self, text):
        self.text_input.set_text(text)
        self.password.set_text("Not time to die")
        self.text_area.set_text("I want to be happy but I'm not sure if I'm in the best path to follow right now in "
                                "my life")

    def set_text_password(self, pwd):
        self.password.set_text(pwd)

    def set_text_area(self, text_area):
        self.text_area.set_text(text_area)
