# Lista de libros (ejemplo)
libros = ["El principito", "It", "Sherlock Holmes", "It", "El principito", "Harry Potter", "It"]

# Diccionario para almacenar los conteos de cada libro
conteo_libros = {}

# Contar la cantidad de veces que se repite cada libro
for libro in libros:
    if libro in conteo_libros:
        conteo_libros[libro] += 1
    else:
        conteo_libros[libro] = 1

# Imprimir el conteo de cada libro
for libro in conteo_libros:
    print(f"{libro}: {conteo_libros[libro]} ejemplar(es)")


