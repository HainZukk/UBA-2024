

def edad_usuario():
    es_correcta = False
    while (not es_correcta):
        try:
            print("Ingrese su edad (solo numeros)")
            edad = int(input())
            es_correcta = True
        except:
            print("No ingresaste un entero. Intenta de nuevo.")
    return edad

edad = edad_usuario()
print("La edad ingresada por el usuario es", edad)
print("Tipo de dato de la edad ingresada:", type(edad))
