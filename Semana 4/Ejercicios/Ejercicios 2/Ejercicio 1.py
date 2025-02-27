def imprimir_vocales(string):
    vocales="aeiuoAEIOU"
    for char in string:
        if char in vocales:
            print(char)

#Ejemplo de uso 
texto=input("Ingrese un texto : ")
imprimir_vocales(texto)
