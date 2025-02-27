# Abrir el archivo en modo escritura ('w')
lista_de_compras = open("compras3.txt", "w")

# Iterar hasta que el usuario ingrese "X"
while True:
    producto = input("Ingrese el producto que necesita comprar (o 'X' para salir): ")
    if producto.upper() == "X":
        break

    # Escribir el producto en el archivo, seguido de un salto de línea
    lista_de_compras.write(producto + "\n")

# Cerrar el archivo después de terminar de escribir
lista_de_compras.close()

print("La lista de compras está guardada")
