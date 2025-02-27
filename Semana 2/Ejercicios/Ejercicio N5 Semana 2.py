#Crear un programa que solicite al usuario 5 enteros y muestre el promedio por pantalla

n = int(input("Ingrese la cantidad de numeros a promediar : "))
suma = 0
i=1
while(i<=n):
    print("Ingrese el numero :  " , i)
    nota = float(input())
    suma = suma + nota
    i+=1
prom = suma / n 
print("El promedio de es :  " , prom)

#Preguntar >D
