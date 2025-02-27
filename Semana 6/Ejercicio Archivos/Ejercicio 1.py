with open("Ejercicio1.txt","r") as file:
    pregunta = file.readline()

#Mostrar pregunta por pantalla
print(pregunta)

#Pedir al usuario que ingrese su respuesta
respuesta = input("Ingrese su respuesta : ")

# Abrir el archivo pregunta.txt en modo de escritura para agregar la respuesta al final
with open("Ejercicio1.txt","a") as file:
    #Escribir respuesta en el archivo
    file.write(respuesta + "\n")


