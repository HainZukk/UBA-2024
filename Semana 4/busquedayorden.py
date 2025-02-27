
personas = [
    ("David Acosta" , 25),
    ("Lautaro Gimenez" , 18),
    ("Jimena Cobe" , 20),
    ("Huynh Nguyen" , 47),
    ("Vanesa Yacanto" , 46),
    ("Dario Barbieris" , 19),
    ("Candela Ipo" , 18),
    ("Santiago Costa" , 19),
    ("Emilse Barte" , 30)
]
#El elemento maria de 25 años esta en personas ?? (la lista)
resultado = ("Dario Barbieris" , 19) in personas        #Esto nos devuelve verdadero o falso 
print(resultado)

#En programacion contamos desde 0 'no olvidarse'
#Para saber la posicion dentro de una lista debemos usar el sigueinte comando :  .index
resultado_1 = personas.index(("Dario Barbieris" , 19))
print(resultado_1)

#Para ordeonar una lista utilizaremos el comando .sort :
        #ej : 
personas.sort()     #dentro de este podemos utilizar parametros como , key reverse etc
print(personas)