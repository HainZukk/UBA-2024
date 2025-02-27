def contar_gustos_diferentes(lista_empanadas):
    #Convierte la lista en un conjunto para eliminar duplicados
    gustos_unicos = set(lista_empanadas)
    #Retorna la cantidad de elementos unicos en el conjuntos
    return len(gustos_unicos)

#Ejemplo de uso 
pedido_empanadas = [
    ("carne"),
    ("pollo"),
    ("queso"),
    ("carne"),
    ("queso"),
    ("cebolla"),
    ("pollo")
]

cantidad_gustos_diferentes = contar_gustos_diferentes(pedido_empanadas)
print("La cantidad de gustos de empanadas son : " , cantidad_gustos_diferentes)