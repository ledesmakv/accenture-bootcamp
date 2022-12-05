from Pages.TextInputPage import TextInputPage

class TestCase():
    # TEST FUNCTIONS
    def test_title(self, init_driver):
        self.TextInputPage = TextInputPage(init_driver)

    def test_button(self, init_driver):
        self.TextInputPage = TextInputPage(init_driver)