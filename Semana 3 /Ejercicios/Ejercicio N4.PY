# Estructuras de control 
        # Crear una funcion que dado un numero , devuelva su valor absoluto

def valor_absoluto(numero):
    if numero < 0:
        return -numero
    else: 
        return numero
    
#ejemplo de uso 
num = -1
resultado = valor_absoluto(num)
print("El valor absoluto es : " ,resultado)

#Explicacion 
             # Esta función valor_absoluto() toma un número como argumento y devuelve su valor absoluto. 
             #Si el número es negativo, se devuelve su opuesto para obtener el valor absoluto. 
             #Si el número ya es positivo, simplemente se devuelve sin cambios.