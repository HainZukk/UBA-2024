#Hacer una lista con 5 nombres y  realizar las siguientes actividades

lista = [
    ("Tobias"),
    ("Marcelo"),
    ("Liz"),
    ("Huynh"),
    ("Vanesa")
]

    # A 
cambiar_ultimo_elemento_lista = lista.remove("Vanesa")
insertar_cambiar_nombre = lista.append("Juan")

#Saber longitud de la lista
longitud = len(lista)
print(longitud)

# b. Devolver el nombre que esté a dos posiciones del final:
#Puedes usar el mismo enfoque de índices negativos para acceder al elemento que esté a dos posiciones del final. Siendo -2 el índice que accede al penúltimo elemento.
nombre_dos_posiciones_del_final = lista[-3]
print("El nombre que está a dos posiciones del final es:", nombre_dos_posiciones_del_final)

# c. Recorrer la lista 
print("Nombres de la lista : ")
for nombre in lista:
    print(nombre)

# d. Imprimir por pantalla con 3 repeticiones
print("Lista con 3 repeticiones:", lista * 3)

print(lista)