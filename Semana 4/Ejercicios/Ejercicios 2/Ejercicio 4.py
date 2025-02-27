def agregar_ingredientes(lista , ingrediente):
    if ingrediente not in lista:
        lista.append(ingrediente)
        print("El ingrediente se añadio exitosamente")
    else:
        print("El ingrediente ya se encuentra en la lista")

#Ejemplo de uso 
lista_ingredientes = [
    ("tomate"),
    ("queso"),
    ("cebolla"),
    ("huevo")
]

nuevo_ingrediente = input(str("Ingrese el ingrediente a agregar : "))
agregar_ingredientes(lista_ingredientes , nuevo_ingrediente)
print("La lista ha sido actualizada : " , lista_ingredientes)