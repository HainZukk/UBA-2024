#Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar,
# imprimiendo un mensaje por pantalla en cada caso.

for numeros in range(1,21):   # for var in iterable(): sintaxis
    if numeros % 2 == 0:   
        print("Es par")
    else: 
        print("Es impar")


