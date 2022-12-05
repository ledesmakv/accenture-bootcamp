from Pages.BasePage import BasePage
# from modulo.archivo import class
from Config.config import TestData

class TextInputPage(BasePage):
    # Los metodos para interactuar especificamente con TextInputPage
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)