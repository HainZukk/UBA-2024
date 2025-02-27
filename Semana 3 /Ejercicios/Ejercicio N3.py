#Determinar si un numero es par y menor a 10 

numero = ("Ingrese un numero par ")
numero_par = int(input("Ingrese el numero : "))

if numero_par % 2 == 0 and numero_par <= 10:
    print ("El numero es par y menor que 10 ")
else:
    print("El numero no es par o no es menor que 10 ")