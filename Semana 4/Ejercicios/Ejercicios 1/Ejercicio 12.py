def almacenar_materias():
    materias = []
    while True:
        materia = input("Ingrese el nombre de la materia (o 'X' para terminar): ")
        if materia.upper() == 'X':
            break  # Salir del bucle si el usuario ingresa 'X'
        materias.append(materia)  # Agregar la materia a la lista
    return materias

# Ejemplo de uso
lista_materias = almacenar_materias()
print("Materias almacenadas:", lista_materias)
