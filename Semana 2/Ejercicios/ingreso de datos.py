#Crear un programa que le solicite un entero
# Y determine si es par mostrando por pantalla un mensaje que indique el resultado

entero = int(input("Ingrese un numero entero : "))

if entero % 2 == 0:         # Decide si determinadas sentencias deben ejecutarse o no
    print("El numero es par")
else :      # Qué hacer en caso de la condición de un if no se cumpla
    print("El numero es impar")