#diccionario = {1: "Hola" , 2: "Chau"}
        #print(diccionario[1])           #Se puede hacer numericamente tambien

#saludos = {             #El diccionario se llama saludos . 
    #"saludo_formal" : "hola buenas tardes como se encuentra usted",
    #"saludo_informal" : "hola como estas",
   # "saludo_cumple" : "feliz cumple"
  #  }

#saludos["saludo_navidad"] = "feliz navidad para todos"

#print(saludos["saludo_navidad"])


        #Otro ejemplo 

amigos = {
    "Tobias" : (18 , "Noviembre") , 
    "Liz" : (18 , "Junio") ,                    #se puede agregar listas adentro de los diccionarios
    "Huynh" : (46 , "Noviembre" , "Nos conocimos en madrid"),
    "Vanesa" : (45 , "Noviembre")
}

print(amigos["Huynh"])

amigos.update(
    {"Huynh" : (46 , "Noviembre" ,"Nos conocimos en cataluña" ) }
)       #Nos sirve para modificar claves anteriores en los diccionarios con .uptdate

print(amigos["Huynh"])