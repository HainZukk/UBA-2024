def guardar_plantas(plantas , especie_nueva , luz_solar , precio_nueva_planta):
    planta_nueva = {
        "especie" : especie_nueva,
        "necesita_luz" : luz_solar ,
        "precio" : precio_nueva_planta

    }
    plantas.append(planta_nueva)

plantas = []
print(plantas)
guardar_plantas(plantas , "Rosa" , True , 5000)
guardar_plantas(plantas , "Jazmin" , True , 6000)
print(plantas)