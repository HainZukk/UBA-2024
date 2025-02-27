#Crear un programar en el que sea imposible ganarle en el juego piedra papel o tijeras cada elemento 
# va a ser representado con una letra R para piedra P para papel y T para tijera 

def jugar():
    print("¡Juguemos! Ingresá piedra (R), papel (P) o tijera (T)")
    jugada = input ()
    if (jugada == "P"):
        print ("Tijera")
    elif (jugada == "R"):
        print ("Papel")
    elif (jugada == "T"):
        print ("Piedra")
    else:
        print("No vale")
jugar()