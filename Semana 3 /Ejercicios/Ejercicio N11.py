def cobro_automatico():    # variable llamada cobro automatico 
    deuda = int(input("Ingrese el monto a cobrar : "))   # le pedimos al usuario que ingrese un numero entero en la variable deuda
    while deuda > 0:   # si deuda es mayor a cero que haga : 
        monto_ingresado = float(input("Ingrese el monto a pagar : ")) # que ingrese el monto a pagar 
        if monto_ingresado <= 0: # si monto ingresado es menor o igual a 0 que : 
            print("Ingrese un valor valido mayor a cero ")   # muestre por pantalla el mensaje 
            continue   #continuar
        
        deuda -= monto_ingresado #significa restar el valor de "monto_ingresado" al valor actual de la variable "deuda".
        if deuda <0: #si deuda es menor a 0 
            cambio = monto_ingresado + deuda # la varibale cambio dice que el monto ingresado sume con la deuda
            print(f"Gracias su cambio es {cambio : }") # y muestre por pantalla el mensaje
        elif deuda == 0: # sino si deuda llega a 0 y se pago totalmente , muestre por pantalla el mensaje print
            print("Gracias su deuda se pago completamente")
        else:   # si falta pagar la deuda (si nada de lo anterior se cumple ) 
            print(f"Falta pagar {deuda : }")  # se mostrara el mensaje que falta pagar tanto para pagar el total de la deuda 

cobro_automatico()   # llamamos a la funcion 


# Preguntar por este ejercicio cuando vaya a clases extras.