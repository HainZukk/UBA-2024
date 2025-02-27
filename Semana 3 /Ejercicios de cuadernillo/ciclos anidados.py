num = int(input("Ingrese un numero entero positivo : "))
while num <= 0:
    num = int(input("Ingrese un numero entero positivo : "))
cant_divisores = 0 
for d in range(2,num//2+1):
    if num % d == 0 :
        cant_divisores +=1
print(num, "tiene" , cant_divisores)