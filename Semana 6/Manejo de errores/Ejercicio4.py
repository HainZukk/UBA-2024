def leer_archivo():
    try:
        with open("file.txt" , "r")as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("No se pudo encontrar el archivo :(")

#llamar a la funcion
leer_archivo()