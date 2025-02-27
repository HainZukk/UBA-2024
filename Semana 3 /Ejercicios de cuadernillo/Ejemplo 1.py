#Contemos cuantos multiplos de 3 ingresan en un lote de 5 numeros
print("ingrese 5 numeros enteros")     #Le damos una pista al usuario de lo que debe ingresar 
total_mult = 0
num = int(input("Numero : "))
if num % 3 == 0:                   #Identifico si es multiplo de 5
    total_mult+=1
num = int(input("Numero : "))
if num % 3 == 0:
    total_mult+=1
num = int(input("Numero : "))
if num % 3 == 0:
    total_mult+=1
num = int(input("Numero :"))
if num % 3 == 0:
    total_mult+=1
num = int(input("Numero : "))
if num % 3 == 0:
    total_mult+=1

print ("Vinieron",total_mult,"Multiplos de 3")
