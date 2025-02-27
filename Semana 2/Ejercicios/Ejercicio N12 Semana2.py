def borrar_letras(palabra , letra):
    palabra_sin_letra = palabra.replace(letra , "") #utilizamos el formato replace para remplazar las letras a nada.
    return palabra_sin_letra

palabra_original = "Manzana"
letras_a_borrar = "a"
#Hacemos el llamado a la funcion con borrar_letras 
palabra_sin_a = borrar_letras(palabra_original , letras_a_borrar)
print(palabra_sin_a) #Imprimimos la palabra sin "A" 