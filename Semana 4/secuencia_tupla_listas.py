
puntos = [              #Creamos una lista
    (4,6),
    (8,2),
    (10,5),                 # Que contiene adentro de la lista tuplas 
    (1,1),
    (0,7),
    (0,0),
    (2,3),
    (2,2),
]


puntos.append((50,50))     

puntos.insert(4,(80,80))            #Porque logramos esto ? Las listas son mutables entonces nos permite cambiar los valores que tenemos
                                                #Adentro en cambio en las tuplas esto no se puede hacer 
puntos.remove((0,7))

for punto in puntos:
    x , y = punto                       #lo logramos gracias al desempaquetamniento de nuestra tupla
    print("x:",x, "- y: ",y)