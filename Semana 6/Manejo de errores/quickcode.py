def pedir_numero_entero():
    while True:
        try:
            numero = int(input("Ingrese un numero entero : "))
            return numero
        except:
            print("El numero ingresado no es un entero valido.")
    
def multiplicar_numeros():
    print("Ingrese un numero entero")
    numero1 = pedir_numero_entero()
    print("Ingrese el segundo numero entero : ")
    numero2 = pedir_numero_entero()
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    suma = numero1 + numero2
    resta = numero1 - numero2
    print(f"La multiplicacion entre {numero1} y {numero2} es {multiplicacion}")
    print(f"La division entre {numero1} y {numero2} es {division}")
    print(f"La suma de {numero1} y {numero2} es {suma}")
    print(f"La resta de{numero1} y {numero2} es {resta}")

multiplicar_numeros()
