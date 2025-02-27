def eliminar_invitado(tupla, nombre):
    # Convertir el nombre a minúsculas
    nombre_minusculas = nombre.lower()
    # Crear una nueva tupla con los nombres convertidos a minúsculas
    nueva_tupla = tuple(elemento for elemento in tupla if elemento.lower() != nombre_minusculas)
    return nueva_tupla

# Ejemplo de uso:
invitados = ("Juan", "María", "Pedro", "Luisa", "Ana")
nombre_a_eliminar = input("Ingrese el nombre del invitado que desea eliminar: ")
invitados_actualizados = eliminar_invitado(invitados, nombre_a_eliminar)
print("Invitados actualizados:", invitados_actualizados)

