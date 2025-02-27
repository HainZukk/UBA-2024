#Crear una funcion que simule un cumpleaños : que dado un entero imprima "Que los cumplas feliz " esa cantidad de veces.
veces = int(input("Ingrese un numero entero : "))
def cumpleaños(veces):
    for _ in range(veces):              #Recordar == o signos de aritmeticas solo validas para operaciones 
        print("Que los cumplas feliz")

resultado = cumpleaños(veces)
print(resultado)
#Utilizamos _ para indicar a python que no estamos usando el iterador i 