# BORJA CANADAS ORTEGA - PSP TAREA 01 -

import unicodedata

def esPalindromo(cadena):
    """
    Determina si una cadena es palíndroma.
    Se eliminan espacios, puntuación, caracteres especiales y diferencias entre mayúsculas y minúsculas.
    """
    # Normalizar la cadena para eliminar tildes y otros diacríticos
    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    cadena_sin_diacriticos = ''.join(
        c for c in cadena_normalizada if unicodedata.category(c) != 'Mn'
    )
    # Eliminar caracteres no alfanuméricos y convertir a minúsculas
    cadena_filtrada = ''.join(filter(str.isalnum, cadena_sin_diacriticos)).lower()
    # Verificar si la cadena filtrada es igual a su reverso
    return cadena_filtrada == cadena_filtrada[::-1]

if __name__ == "__main__":
    frase = input("Introduce una frase para comprobar si es palíndroma: ")
    if esPalindromo(frase):
        print("La frase es palíndroma.")
    else:
        print("La frase no es palíndroma.")
