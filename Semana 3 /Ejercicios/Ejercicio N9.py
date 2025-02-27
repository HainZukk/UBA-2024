#Crear una funcion que reciba un numero entero e imprima por pantalla la tabla de ese numero del 1 al 10 

numero = int(input("Ingrese el numero entero : "))

def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i 
        print(f"{numero} x {i} = {resultado}")

tabla_multiplicar(numero)

