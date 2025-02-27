# Se quiere hacer un programa que le solicite al usuario un número divisor y un dividendo, y calcule el cociente entre ellos.
        #AYUDA: Considerar que el usuario podría brindar un valor no numérico o un divisor nulo.

def pedir_numeros():
    while True:
        try:
         numero =  int(input("Ingrese el numero : "))
         return numero
        except:
           print("El numero ingresado no es correcto")

def pedir_divisor_y_dividendo():
   print("ingrese un numero entero : ")
   divisor = pedir_numeros()
   print("Ingrese el dividendo : ")
   dividendo = pedir_numeros()
   total = divisor / dividendo
   print(f"El resultado de {divisor} entre {dividendo} es {total} ")

pedir_divisor_y_dividendo()
