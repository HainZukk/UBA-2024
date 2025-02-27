def pedir_numero_entero():
    while True:
        try:
            numero = int(input("Ingrese un numero entero : "))
            return numero
        except:
            print("El numero entero ingresado no es correcto")

def calcular_el_producto():
    print("Ingrese el primer numero entero : ")
    numero1 = pedir_numero_entero()
    print("Ingrese el segundo numero entero : ")
    numero2 = pedir_numero_entero()
    producto = numero1 * numero2
    print(f"El producto de {numero1} y {numero2} es {producto}")

calcular_el_producto()