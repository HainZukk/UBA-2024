def obtener_cociente_resto(dividiendo , divisor):
    cociente = dividiendo // divisor 
    resto = dividiendo % divisor 
    return cociente, resto 

#Ejemplo uso de la funcion
dividiendo = 10
divisor = 3
cociente , resto = obtener_cociente_resto(dividiendo, divisor)
print("El cociente de la division es :" , cociente)
print("El resto de la division es : ", resto)