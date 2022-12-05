from Pages.basePage import BasePage
# from modulo.archivo import class
from Config.config import TestData
from Config.locators import Locators

class TextInputPage(BasePage):

# Los metodos para interactuar especificamente con textInputPage

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def get_page_title(self):
        return self.get_title()

    def do_exercise(self, value):
        self.do_send_keys(Locators.text_input, value)
        self.do_click(Locators.text_button)
        text = self.get_element_text(Locators.text_button)
        return text