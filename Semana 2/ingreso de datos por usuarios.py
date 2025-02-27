# Para el ingreso de datos por los usuarios necesitaremos el comando Input

#print("ingrese un valor: ")
valor = input("Ingrese un valor: ")
print(valor)
print(type(valor))



#Enterios / INT ej
numero = int(input("Ingrese un numero: ")) # le decimos que solo ingrese numeros enteros no strings ni floats (int)
otro_numero = int(input("ingrese su otro numero: "))

# int 
# str
# floats

suma = numero + otro_numero             # ojota con concatenar el string
print(suma)

#Strings / STR ej 
plc = str(input("Ingrese un valor porfavor : "))
dlc = str(input("ingrese otro valor por favor : "))

sumados = plc + dlc
print(sumados)

#Flotantes / floats ej 
qsy = float(input("INGRESE UN CARACTER : "))
qsi = float(input("INGRESE OTRO VALOR : "))
sumatres = qsy + qsi
print (sumatres)




