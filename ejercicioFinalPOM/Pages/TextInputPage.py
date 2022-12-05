from Pages.BasePage import BasePage
from Config.config import TestData
from Config.locators import Locators

class TextInputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def get_page_title(self):
        return self.get_title()

    def click_sampleapp_link(self):
        self.do_click(Locators.sampleapp_link)

    def do_exercise(self, user, password):
        self.do_send_keys(Locators.username_input, user)
        self.do_send_keys(Locators.password_input, password)
        self.do_click(Locators.text_button)
        label = self.get_element_text(Locators.text_label)
        return label