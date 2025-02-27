def mostrar_valor_lista(lista , indice):
    try:
        valor = lista[indice]
        print(f"El valor en el indice {indice} es {valor} ")
    except IndexError:
        print(f"Índice {indice} fuera del rango. La lista tiene {len(lista)} elementos.")

#ejemplo de uso 
mi_lista = [10,20,30,40,50]

mostrar_valor_lista(mi_lista , 0)
