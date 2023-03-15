from seleniumpagefactory import PageFactory


class FormSubmitted(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    locators = {
        'title': ('XPATH', "//h1[normalize-space()='Form submitted']"),
        'msg': ('CLASS', "lead")
    }

    