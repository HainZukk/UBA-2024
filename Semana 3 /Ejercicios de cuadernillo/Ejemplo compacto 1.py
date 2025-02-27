#Ingresar 5 numeros enteros
print("Ingrese 5 numeros enteros ")
total_mult = 0 
veces = 1           #Si lo cambiamos a 0 nos pedira 6 numeros no 5 :D
while veces <= 5:
    num = int(input("Numero : "))
    if num % 3 == 0:
        total_mult+=1
    veces+=1
print ("Vinieron " ,total_mult ,"Multiplos de 3 " )

