def tareas_de_manuel(lista_actividades):
    tareas_manuel = [num for num in lista_actividades if num % 2== 0]
    return tareas_manuel

#Ejemplos de uso 
lista_actividades = [1,2,3,4,5,6,7,8,9]
tareas_manuel = tareas_de_manuel(lista_actividades)
print("Las tareas de manuel son : " , tareas_manuel)