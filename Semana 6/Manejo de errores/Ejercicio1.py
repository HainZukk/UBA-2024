def pedir_numero():
    numero = input("Ingrese un numero entero valido : ")
    if numero.isnumeric():
        print(f"El numero ingresado es {int(numero)}")
    else:
        print("El numero ingresado no es un numero valido.")

pedir_numero()