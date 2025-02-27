pais1=("Francia" , "Paris" , "Europa")
pais2=("Argentina" , "Buenos Aires" , "America")
pais3=("Japon" , "Tokio" , "Asia")
pais4=("Alemania" ,"Berlin" , "Europa")
pais5=("Peru" , "Lima" , "America")

lista_con_paises = [
    pais1,
    pais2,
    pais3,
    pais4,
    pais5
]

#Creamos la funcion 
def imprimir_info_paises(lista):
    for pais in lista:
        print("Pais : " ,pais[0])
        print("Capital : " , pais[1])
        print("Continente" , pais[2])
        print()

#Llamar a la funcion 
imprimir_info_paises(lista_con_paises)