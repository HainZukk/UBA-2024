palabra_a_modificar = input("Ingrese la palabra a modificar : ")
palabra_modificada = input("Ingrese la palabra por la cual quiere sustituir : ")

#Nombre del archivo 
nombre_archivo = "letra4.txt"
try:
#leer el archivo 
    with open("letra4.txt" , "r") as file:          #le cambia el nombre de  letra4.txt ----> file
        contenido = file.read().lower()     
    if palabra_a_modificar not in contenido:
        print(f"La palabra {palabra_a_modificar} no se encontro en el texto")
    else:
        contenido_modificado = contenido.replace(palabra_a_modificar,palabra_modificada)

    #Guardar modificaciones
        with open("letra4.txt","w") as file:
          file.write(contenido_modificado)
    print("Se actualizo el texto exitosamente")


except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no se encontro")
    

#Acordarme de cd "Python Facu/Semana 6/" etc