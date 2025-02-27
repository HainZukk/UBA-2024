def combinar_string_enterio(texto , numero):

    #Convertir el entero a string
    numero_str=str(numero)
    #Combinar el string y el entero dentro de un string
    resultado = texto + numero_str

    return resultado

#Ejemplo de uso de la funcion
texto="Numero : "
numero = 42
resultado = combinar_string_enterio(texto , numero)
print(resultado) #Esto imprimira "Numero : 42"

