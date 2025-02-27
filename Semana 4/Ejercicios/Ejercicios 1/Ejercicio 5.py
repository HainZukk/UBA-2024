#Crear una tupla que guarde tu nombre y apellido y tu edad , Luego , imprimir por pantalla tu edad accediendo de la tupla
        # que corresponda

#fecha = ("Tobias" , "Nguyen" , 18)
        #Creamos la siguiente variable
#nombre,apellido,edad = fecha

#print(edad)


#Ejemplo con input
# Crear una tupla que guarde nombre, apellido y edad
informacion_personal = ("Tobias", "Nguyen", 18)

# Solicitar al usuario que ingrese qué información desea ver
opcion = input("¿Qué información deseas ver? (nombre / apellido / edad): ")

# Convertir la entrada del usuario a minúsculas para facilitar la comparación
opcion = opcion.lower()

# Verificar la opción seleccionada por el usuario y mostrar la información correspondiente
if opcion == "nombre":
    print("El nombre es : " , informacion_personal[0])
elif opcion == "apellido":
    print("El apellido es : " , informacion_personal[1])
elif opcion == "edad":
    print("La edad es : ", informacion_personal[2])
else:
    print("Ingrese una opcion valida")
