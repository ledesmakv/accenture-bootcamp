class BasePage:
# La super class, parent class, funciones que comparten el resto de las paginas, de la cual heredan el resto de las paginas

    # INITIALIZER
    def __init__(self, driver):
        self.driver = driver

    # Methods