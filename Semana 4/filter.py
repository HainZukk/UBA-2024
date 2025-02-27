def es_palabra_corta(palabra):
    longitud = len(palabra)
    if (longitud < 5):
        return True
    else:
        return False

def es_palabra_larga(palabra):
    longitud = len(palabra)
    if (longitud < 5):
        return False
    else:
        return True

palabras = (
    "perro",
    "mesa",
    "silla",
    "auto",
    "planta",
    "arbol",
    "plata"
)

palabras_cortas = list(filter(es_palabra_corta , palabras))

palabras_largas = list(filter(es_palabra_larga , palabras))


print(palabras_cortas)
print(palabras_largas)