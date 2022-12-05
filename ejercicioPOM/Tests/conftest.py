import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Config.config import TestData

# Creamos la instancia de la sesion del browser y lo tiramos abajo
# La instancia se crea por Class
@pytest.fixture(scope="class")
def init_driver():
    if TestData.browser == "Chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver # Devuelve la instancia del driver
    driver.quit()