def filtrar_mejores_peliculas(diccionario_peliculas):
    mejores_peliculas = []
    for pelicula in diccionario_peliculas:
        if pelicula["Puntuación"] > 7:
            mejores_peliculas.append(pelicula)
    return mejores_peliculas

# Ejemplo de uso:
peliculas_de_sol = [
    {"Nombre de la película": "Titanic", "Año": 1997, "Puntuación": 9},
    {"Nombre de la película": "El Padrino", "Año": 1972, "Puntuación": 10},
    {"Nombre de la película": "El Señor de los Anillos", "Año": 2001, "Puntuación": 8},
    {"Nombre de la película": "La La Land", "Año": 2016, "Puntuación": 6}
]

mejores_peliculas_de_sol = filtrar_mejores_peliculas(peliculas_de_sol)
print("Las mejores películas según Sol son:")
for pelicula in mejores_peliculas_de_sol:
    print(pelicula)
