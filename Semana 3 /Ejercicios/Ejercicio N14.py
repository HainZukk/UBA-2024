#Preguntar el esto en clases

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2 , int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
def primos_hasta(n):
    for num in range(2 , n + 1):
        if es_primo(num):
            print(num)
            
numero = 30
primos_hasta(numero)

