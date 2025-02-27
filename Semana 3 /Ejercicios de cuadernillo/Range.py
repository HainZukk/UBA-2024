#Sintaxis de range
                # range(valor_inicial , valor_fin , paso)

        #El paso debe ser entero 
            #Valor_inicio esta incluido en el rango ; valor_fin NO
               #Valor_inicio es opcional , si no se coloca se asumen 0 
                    #Paso es opcional , si no se coloca asumen 1 
                            # Si se desea rango decreciente se debe colocar un rango negativo 
                                      # Si se coloca un paso , DEBE COLOCAR valor_inicio aunque este ultimo sea 0


# Ejemplos de uso de rango 
                # Range(1,10) ----> 1,2,3,4,5,6,7,8,9
                    # Range(6) -----> 0,1,2,3,4,5
                         # Range (0,,8,2) -----> 0,2,4,6
                                  # Range (15,10,-5) ----> 15
                                          # Range (15,10,-1) -------> 15,14,13,12,11


#Contemos cuantos multiplos de 3 ingresan en un lote de 5 numeros enteros. 
print("Ingrese 5 numeros enteros ")
total_mult = 0 
for vuelta in range (5):
    num = int(input("Numero : "))
    if num % 3 == 0:
        total_mult+=1
print("Vinieron " , total_mult , " Multiplos de 3 ")


#El ciclo for tambien puede iterar sobre elementos de una lista como por ejemplo . 
        #Lista de numeros 
numeros = (11,24,32,4,15,6,17,38,34,94,110)
for numero in numeros:
    print(numero)



#Ejemplo de continue and break 

#Lista de numeros 
numeros = [1,2,3,4,5,6,7,8,9,10]

#Bucle for para encontrar el primer numero divisible por 7 en la lista 
for numero in numeros:
    if numero % 7 == 0:
        print ("El primer numero divisible por 7 es : " ,numero )
        break

#Continue 
numeros = [1,2,3,4,5,6,7,8,9,10]

#Bucle for para imprimir los numeros impares de la lista 
for numero in numeros:
    if numero % 2 == 0:
        #Si es par , saltar a la siguiente iteracion
        continue
    print(numero)

