numero = int(input("Ingrese un numero entero : "))  # Le pedimos al usuario que ingrese un numero entero 
while numero < 3:             # Condicion 
    print(numero)
    numero += 1

if numero == 3:       #Traduccion : si el numero es igual a 3 muestra por pantalla "Es tres"
    print("Es tres") 

else:                    #Traduccion : sino muestra por pantalla "El numero no es tres"
    print("El numero no es tres")   # Podemos quitar este else ya que nunca se ejecutara .  