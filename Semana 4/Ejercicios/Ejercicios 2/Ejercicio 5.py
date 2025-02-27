def insertar_en_orden(lista, nuevo_entero):
    # Iteramos sobre la lista para encontrar la posición adecuada donde insertar el nuevo entero
    for i in range(len(lista)):
        if nuevo_entero >= lista[i]:
            lista.insert(i, nuevo_entero)
            return

    # Si el nuevo entero es menor que todos los elementos de la lista, lo agregamos al final
    lista.append(nuevo_entero)

# Ejemplo de uso:
mano_de_cartas = [10, 8, 6, 4, 2]
nueva_carta = int(input("Ingrese el valor de la nueva carta : "))
insertar_en_orden(mano_de_cartas, nueva_carta)

print("Mano de cartas actualizada:", mano_de_cartas)
