opciones = {
    1: "hamburguesas",
    2: "milanesas",
    3: "gaseosa",
    4: "alfajor",
    5: "papas fritas",
    6: "agua"
}

valores = {
    1:1000,
    2:1500,
    3:500,
    4:300,
    5:600,
    6:350
}

def mostrar_menu():
    print("Menu : ")
    for codigo , producto in opciones.items():
        print(f"{codigo} : {producto} -> {valores[codigo]}")
        
def solicitar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese el codigo del producto que desea comprar : "))
            if opcion in opciones:
                return opcion
            else:
                print("La opcion no es valida , ingrese un codigo valido")
        except:
            print("Entrada no valida . Por favor ingrese un numero ")
       
#Creamos una funcion que solicite la cantidad que desea comprar         
def solicitar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad que desea comprar : "))
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser un numero positivo ")
        except ValueError:
            print("Entrada no valida . Por favor ingrese un numero : ")
            
def main():
    mostrar_menu()
    opcion = solicitar_opcion()
    cantidad = solicitar_cantidad()
    total = valores[opcion] * cantidad 
    print(f"Ha seleccionado {cantidad} {opciones[opcion]}(s) . El total a pagar es ${total}")

if __name__ == "__main__":
    main()