
#Ejemplo con map()          sintaxis map(funcion,secuencia)
#def cuadrado(numero):
    #return numero * numero 

#lista = [3,6,1,2]
#print("Lista : " , lista)

#nueva_lista = list(map(cuadrado , lista))           #Ponemos list ya que map nos da un mapa no una lista . 
#print("Nueva lista : " , nueva_lista)

#Ejemplo con filter()           sintaxis filter(funcion, secuencia)

        #Ej queremos quedarnos con las palabras que empiecen con M

#def empieza_con_m(palabra):
 #   return palabra[0] == 'm'

#lista = ["manzana" ,"balde" , "molde" , "marron " , "carro " ]
#print("lista : " )
#for i in lista:
 #   print(i)

#print()

#nueva_lista_2_0 = list(filter(empieza_con_m , lista))
#print("Nueva lista : " )
#for n in nueva_lista_2_0:
 #   print(n)


#Otro ejemplo con filter and map 

def cuadrado(x):
    return x ** 2 

def par(x):
    if x%2==0:
        return True
    else:
        return False
    
lista = [1,2,3,4,5,6]

print('Lista original : ')
print(lista)

lis = list(map(cuadrado , lista))
print("lista de cuadrados : ")
print(lis)

filtro = list(filter(par,lista))
print("Lista de pares : ")
print(filtro)