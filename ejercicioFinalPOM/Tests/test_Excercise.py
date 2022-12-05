from Pages.TextInputPage import TextInputPage
from Config.config import TestData
import pytest

class TestCase():
    # Ingreso a la Homepage y verifico que coincida el Title
    def test_title(self, init_driver):
        self.TextInputPage = TextInputPage(init_driver)
        title = self.TextInputPage.get_page_title()
        assert title == TestData.page_title, "El title no coincide"

    # Clickeo en el button Sample App y verifico que coincida el Title
    def test_sampleapp_title(self, init_driver):
        self.TextInputPage = TextInputPage(init_driver)
        self.TextInputPage.click_sampleapp_link()
        title = self.TextInputPage.get_page_title()
        assert title == TestData.sampleapp_title, "El title no coincide"

    @pytest.mark.parametrize("username, password, expected_result", [("Kari", "pwd", "Welcome, Kari!"), ("", "pwd", "Invalid username/password"), ("Kari", "a", "Invalid username/password"), ("", "", "Invalid username/password"), ("", "a", "Invalid username/password"), ("Kari", "", "Invalid username/password")])
    def test_successful_login(self, init_driver, username, password, expected_result):
        self.TextInputPage = TextInputPage(init_driver)
        self.TextInputPage.click_sampleapp_link()
        label = self.TextInputPage.do_exercise(username, password)
        assert expected_result == label, "Error en Login"