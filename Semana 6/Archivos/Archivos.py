archivo = open("archive.txt")
lineas = archivo.readlines()
archivo.close()

#Dado un archivo lo leimos / lo pasamos a una variable y trabajamos con ese archivo linea a linea
contador = 0
for linea in lineas:
    if "zamba" in linea:
        contador += 1

print("La palabra zamba " , contador , "se repite")