def division(dividendo , divisor): 
    if divisor == 0:                    #Si el divisor es 0 
        return "Error"                                  #Devuelvo el mensaje error
    else:
        resultado = dividendo / divisor
        return resultado  

resultado_division= division(10,2)     #Aqui hacemos el llamado a la funcion 
print(resultado_division)   # Aqui imprimimos por pantalla el resultado y llamamos la variable creada anteriornente.
    
#Ejemplo de buena practica 
#def division(dividiendo , divisor):
 #   if divisor ==0:
        #return "error"
    
  #  return dividiendo / divisor