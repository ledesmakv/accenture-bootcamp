import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Config.config import TestData

@pytest.fixture(scope="class")
def init_driver():
    if TestData.browser == "Chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()