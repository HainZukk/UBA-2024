def unir_palabras(lista):
    # Inicializamos una cadena vacía para almacenar la frase
    frase = ""
    # Recorremos la lista de palabras en orden inverso
    for palabra in reversed(lista):
        # Agregamos la palabra seguida de un espacio a la frase
        frase += palabra + " "
    # Eliminamos el espacio extra al final de la frase y retornamos
    return frase.strip()

# Ejemplo de uso
lista_palabras = ["entender", "pueden", "humanos", "los", "que", "código", "escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código", "escribe", "tonto", "Cualquier"]
frase = unir_palabras(lista_palabras)
print(frase)

