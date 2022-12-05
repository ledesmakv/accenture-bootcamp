# Importamos el paquete de Selenium y Webdriver para poder implementar sus clases y metodos, interaccion con el navegador
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Importamos By para elegir locator strategy
from selenium.webdriver.common.by import By
import time

# Creamos la sesion de Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Acceder a la URL 
driver.get('https://google.com')

# Identifico el Input con el que quiero interactuar
search_field = driver.find_element(By.CLASS_NAME, "gLFyf")
# Borrar texto que viene por Default
search_field.clear()

# Le envio el valor Selenium que es lo que queremos buscar
search_field.send_keys("selenium")

# Identifico el boton en el cual quiero hacer click para realizar la busqueda
search_button = driver.find_element(By.XPATH, '//div[@class="FPdoLc lJ9FBc"]//input[@name="btnK"]')
search_button.click()
time.sleep(3)

# Identificar los titulos de la busqueda que realice, guardarlos o almacenarlos en una lista
# Me guardo 31 elementos web
# Identifico varios elementos, devuelve una lista de ellos
heading_list = driver.find_elements(By.XPATH, '//h3[@class="LC20lb MBeuO DKV0Md"]')

i = 0
for heading in heading_list:
    print(heading.get_attribute("textContent"))
    i += 1
    if (i > 4):
        break

# Cerramos la instancia del browser
driver.quit()
