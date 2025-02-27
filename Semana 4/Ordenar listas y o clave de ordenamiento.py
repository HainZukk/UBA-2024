def edad(persona):              #Creamos una variable llamada persona      
    return persona[1]               #Le pedimos que regrese la edad de las personas a partir de la segunda secuencia ej (

   # David Acosta la segunda secuencia seria su edad 25  )          David seria (0) y 25 seria (1)

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

personas.sort(key=edad , reverse=True)      #Le pedimos que organize por edad 
print(personas)