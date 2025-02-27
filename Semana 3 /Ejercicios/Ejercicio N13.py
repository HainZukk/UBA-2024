def empezar_jugada(cant_fichas):
    fichas_ingresada = 0
    while (fichas_ingresada < cant_fichas):
        fichas_faltantes = cant_fichas - fichas_ingresada
        print(f"Ingresa {cant_fichas} fichas para comenzar . Fichas faltantes : {fichas_faltantes}")
        letra = input().lower()
        if (letra == "f"):
            fichas_ingresada = fichas_ingresada +1
        else:
            print("Ingrese solamente fichas reales (F)!")

empezar_jugada(3)


#Preguntar por este ejercicio 