#Ejemplo calculo de pago por horas
cant_horas = int(input("Ingrese la cantidad de horas trabajadas : "))
valor_hora = float(input("Ingrese valor de la hora de trabajo : "))
hijos = input("Tiene hijos (si/no) : ")
total = cant_horas * valor_hora
if hijos == "si":                                                                   #Anidamiento de if 
    plus_fijo = float(input("Ingrese adicional de guarderia : "))
else :                                                                                  
    if (cant_horas >= 30):                                                          
        total * 1.1
print("Debe cobrar" , total)

