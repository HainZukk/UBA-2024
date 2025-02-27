# Recibe el nombre de una persona y la saluda
def saludar(nombre):
    print("Hola " + nombre + " Espero que estes bien ")


saludar("Vanesa")   # ejemplo
saludar("Liz")        # ejemplo

# Sintaxis para crear una funcion es def


# Otra forma de utilizar funcion es con el caracter , (Coma)
# Recibe 2 numeros e imprime la suma por pantalla
def mostrar_suma(sumando_1, sumando_2):   # NO OLVIDARME DE LOS (:)
    suma = sumando_1 + sumando_2        # No mas de 7 u 8 parametros para no afectar a la legibilidad de mi codigo
    print("La suma es: ", suma)

mostrar_suma(10, 3)


#Uso del RETURN
#Recibe 2 numeros y devuelve la suma de ellos
def suma(sumando_1, sumando_2):
    resultado = sumando_1 + sumando_2
    return resultado
#Comando return nos sirve para devolver la informacion / parametros

# Varible seria resultado_suma
resultado_suma = suma(5, 9)
print(resultado_suma)

# Como devolver 1 o mas parametros
# Recibe 2 numeros y devuelve la suma y la resta de ellos
def resultados(numero_1, numero_2):
    suma= numero_1 + numero_2     #parametro 1 
    resta = numero_1 - numero_2     #parametro 2
    return suma, resta

suma , resta = resultados(30 , 18)
print("La suma es :", suma)
print ("La resta es :", resta)