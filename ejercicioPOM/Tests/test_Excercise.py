# Nombre de las carpetas en mayuscula
# Nombre de los archivos en minuscula
# Nombre de las clases en mayuscula
# from carpeta.archivo import class
from Pages.textInputPage import TextInputPage
from Config.config import TestData
import pytest

class TestCase():
    # TEST FUNCTIONS
    def test_title(self, init_driver):
        self.TextInputPage = TextInputPage(init_driver)
        title = self.TextInputPage.get_page_title()
        # title = me lo traje de la pagina
        # TestData.page_title es la variable que tengo en el archivo config, mi expected result
        print(title)
        # Hacer un assert del Title
        assert title == TestData.page_title, "El title de textInputPage no es correcto"

    # 1° escenario: que de pass, actual result = expected result
    # 2° escenario: que falle, actual result != expected result
    @pytest.mark.parametrize("actual_result, expected_result", [("Texto de prueba", "Texto de prueba"), ("Texto diferente", "Texto de prueba")])
    def test_button(self, init_driver, actual_result, expected_result):
        self.TextInputPage = TextInputPage(init_driver)
        # Hacer input en el text box: necesito para interactuar con ese elemento
        # Hacer click en el boton
        # Hacer un assertion del text del boton
        text = self.TextInputPage.do_exercise(actual_result)
        # Comparamos contra TestData.page_title para que falle, despues lo cambiamos
        # En consola corremos "pytest ruta-de-archivo -n 3" para ejecutar los 3 tests a la vez
        assert text == expected_result, "El texto del button no se actualizo"