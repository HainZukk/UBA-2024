#Crear una funcion dada una letra , imprima por pantalla la estacion del año que respresenta
letra1 = ("Ingrese una letra")
letra = input("Ingrese la letra : ")

def estacion (letra):
    if letra == "V":
        print("Verano")
    elif letra == "O":
        print ("Otoño")
    elif letra == "I":
        print("Invierno")
    elif letra == "P":
        print ("Primavera")
    else:
        print("Error")

resultado = estacion(letra)        #Hacemos el llamado a la funcion 
print(resultado)
    
