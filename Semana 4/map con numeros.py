
palabras = (
    "perro",
    "mesa",
    "silla",
    "auto",
    "planta",
    "arbol",
    "plata"
)


def sumar_uno(numero):
    return numero + 1

numeros = [1,2,3,4,5,6,7,8,9]

#creamos una variable
nuevos_numeros = list(map(sumar_uno,numeros))

print(numeros)
print(nuevos_numeros)