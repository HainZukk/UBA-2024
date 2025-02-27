#Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de ambos es menor a 100, 
#calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con ese valor. Si la suma es mayor a 100, 
#mostrar un mensaje diciendo “Llega a 100”.

ingresodenumero1 = ("ingrese 2 numeros entero ")
num_1 = int(input("Ingrese el numero : "))                          #Esto lo hice particularmente yo 
num_2 = int(input("Ingrese el segundo numero : "))

def suma_menor_100(num_1,num_2):
    suma = num_1 + num_2
    if suma < 100:
        diferencia = 100 - suma
        return f"Faltan {diferencia} para llegar a 100"             #f para format . 
    else:
        return "Llega a 100"
    
resultado = suma_menor_100(num_1,num_2)
print(resultado)