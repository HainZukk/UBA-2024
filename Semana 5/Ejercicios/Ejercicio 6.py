def filtrar_productos(lista_productos):
    # Lista para almacenar los productos eliminados
    productos_eliminados = []
    
    # Filtrar productos que pasaron el chequeo de calidad
    productos_filtrados = [producto for producto in lista_productos if producto['pasado']]

    # Contar la cantidad de elementos restantes
    cantidad_elementos = len(productos_filtrados)
    
    # Crear la tupla con los elementos eliminados y la cantidad de elementos restantes
    resultado = (productos_eliminados, cantidad_elementos)
    
    return resultado

# Ejemplo de uso
productos = [
    {'codigo': 1, 'fecha_vencimiento': '2024-05-10', 'pasado': True},
    {'codigo': 2, 'fecha_vencimiento': '2024-05-15', 'pasado': False},
    {'codigo': 3, 'fecha_vencimiento': '2024-05-20', 'pasado': True},
    {'codigo': 4, 'fecha_vencimiento': '2024-05-25', 'pasado': False}
]

resultado = filtrar_productos(productos)
print("Elementos eliminados:", resultado[0])
print("Cantidad de elementos restantes:", resultado[1])


#Preguntar en taller 