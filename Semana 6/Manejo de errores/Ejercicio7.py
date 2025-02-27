#Crear una funcion que pida al usuario informar el numero de jugadores
def jugar_truco():
    while True:
        try:
            players = int(input("Ingrese la cantidad de jugadores : "))
            if players < 2 :
                print("Debe haber al menos 2 jugadores")
            elif players > 6:
                print("Se puede jugar con un maximo de 6 jugadores")
            elif players % 2 != 0:
                print("Debe haber un numero par de jugadores")
            else:
                print(f"La cantidad de {players} jugadores es compatible con el juego , puede comenzar")
                return players
        except ValueError:
            print("El caracter que ingreso no es un numero")
            
jugar_truco()