#Solicitar al usuario su año de nacimiento y otro año 
anio_nacimiento = int(input("Ingrese su año de nacimiento : "))
anio_deseado = int(input("Ingrese el año del cual desea saber la edad : "))

#Calcular la edad 
edad = anio_nacimiento - anio_deseado 

#Imprimir la edad de la persona 
print("El año" , anio_deseado , "tenias" , edad , "años")
