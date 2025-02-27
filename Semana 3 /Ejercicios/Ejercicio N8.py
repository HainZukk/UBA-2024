#Crear una funcion que reciba un numero entero e imprima por pantalla los numeros del 1 hasta ese numero con la estructura de control
            #Iterativa for 

pedir_numero = ("Ingrese un numero entero")
numero = int(input("ingrese el numero entero : "))

def contar_hasta(numero):
    for i in range(1 , numero +1):
        print(i)

resultado = contar_hasta(numero)
print(resultado)