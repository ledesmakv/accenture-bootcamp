from selenium.webdriver.common.by import By

class BasePage():
# La super class, parent class, funciones que comparten el resto de las paginas, de la cual heredan el resto de las paginas

    # INITIALIZER
    def __init__(self, driver):
        self.driver = driver

    # Methods
    def get_title(self):
        # Me devuelve el Title
        return self.driver.title

    def find_element_xpath(self, locator):
        # Identifico a traves de xpath el elemento web con el que quiero interactuar
        # Para usar el By.XPATH tengo que importar from selenium.webdriver.common.by import By
        return self.driver.find_element(By.XPATH, locator)

    def do_send_keys(self, locator, value):
        # Guardo en una variable el elemento web con el que quiero interactuar
        element = self.find_element_xpath(locator)
        # Le hago el send_keys al elemento web
        element.send_keys(value)

    def do_click(self, locator):
        element = self.find_element_xpath(locator)
        element.click()

    def get_element_text(self, locator):
        element = self.find_element_xpath(locator)
        text = element.text # Otra forma de obtener el texto es -> element.get_attribute("textContent")
        return text