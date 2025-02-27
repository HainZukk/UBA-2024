def pedir_numeros_con_try():
    try:
        numero = int(input("Ingrese un numero entero valido : "))
        print(f"El numero ingresado es {numero} ")
    except:
        print("El numero ingresado no es un numero entero valido.")

pedir_numeros_con_try()
