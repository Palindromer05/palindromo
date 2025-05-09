# BORJA CANADAS ORTEGA - PSP TAREA 01 -

import unittest
# Esta librería se utiliza para escribir y ejecutar pruebas automáticas.

from charfun import esPalindromo
# Importa la función `esPalindromo` desde el archivo `charfun.py` para ser probada.

class TestPalindromo(unittest.TestCase):
    # Se define una clase `TestPalindromo` que hereda de `unittest.TestCase`.
    # Esta clase agrupa todas las pruebas relacionadas con la función `esPalindromo`.

    def test_palindromo_valido(self):
        # Prueba si la función identifica correctamente una frase palíndroma simple.
        self.assertTrue(esPalindromo("Anita lava la tina"))
        # `assertTrue` verifica que el resultado de `esPalindromo` sea `True`.

    def test_palindromo_vacio(self):
        # Prueba cómo se comporta la función con una cadena vacía.
        self.assertTrue(esPalindromo(""))
        # Una cadena vacía se considera palíndroma, ya que no hay nada que comparar.

    def test_palindromo_un_caracter(self):
        # Prueba cómo se comporta la función con una cadena de un solo carácter.
        self.assertTrue(esPalindromo("a"))
        # Cualquier cadena de un solo carácter se considera palíndroma.

    def test_palindromo_numeros(self):
        # Prueba si la función identifica correctamente cadenas numéricas palíndromas.
        self.assertTrue(esPalindromo("12321"))
        # Verifica que una cadena de números palíndroma sea detectada como tal.
        self.assertFalse(esPalindromo("12345"))
        # Verifica que una cadena de números no palíndroma sea correctamente identificada como no palíndroma.

    def test_palindromo_caracteres_especiales(self):
        # Prueba si la función maneja correctamente frases con caracteres especiales y acentos.
        self.assertTrue(esPalindromo("¿acaso hubo búhos acá?"))
        # Verifica que los caracteres especiales y acentos sean ignorados correctamente.
        self.assertTrue(esPalindromo("¡Anita, lava la tina!"))
        # Verifica que la función ignore puntuación como signos de exclamación.

    def test_palindromo_invalido(self):
        # Prueba si la función identifica correctamente frases no palíndromas.
        self.assertFalse(esPalindromo("Hola mundo"))
        # Verifica que una frase no palíndroma sea detectada correctamente.
        self.assertFalse(esPalindromo("Python es genial"))
        # Verifica que otra frase no palíndroma sea detectada correctamente.

if __name__ == "__main__":
    # Este bloque garantiza que las pruebas se ejecuten solo si el archivo es ejecutado directamente.
    unittest.main()
    # Ejecuta todas las pruebas definidas en la clase `TestPalindromo`.
    # Genera un reporte en la consola indicando qué pruebas pasaron o fallaron.
