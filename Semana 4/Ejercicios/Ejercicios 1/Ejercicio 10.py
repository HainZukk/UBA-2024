# Crear una lista con los números del 1 al 10
numeros = list(range(1, 11))

# Crear una lista para almacenar los números elevados al cuadrado
cuadrados = []

# Recorrer la lista original y guardar los números elevados al cuadrado en la nueva lista
for numero in numeros:
    cuadrado = numero ** 2
    cuadrados.append(cuadrado)

# Imprimir la lista de números elevados al cuadrado
print("Lista de números elevados al cuadrado:", cuadrados)
