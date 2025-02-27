# Crear una funcion que pida al usuario informar el numero de jugadores 

#Crear la funcion 
def jugar_chinchon():
    while True:
        try:
            print("Recuerde que la cantidad maxima son 4 y minima 2")
            cant_jugadores = int(input("Ingrese la cantidad de jugadores : "))
            if cant_jugadores < 2:
                print("Deben ser al menos 2 jugadores")
            elif cant_jugadores > 4:
                print("Se puede jugar con un maximo de 4 jugadores")
            else:
                print(f"Los jugadores son {cant_jugadores} , pueden comenzar :D ")
                return cant_jugadores
        except:
            print("El caracter ingresado no es correcto !") 
            
jugar_chinchon()