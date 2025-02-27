# Definición de los maratonistas
maratonistas = {
    '12345678A': {
        'nombre': 'Juan',
        'maratones': [
            {'nombre': 'Maratón de Madrid', 'año': 2020, 'puesto': 5, 'tiempo': '2:30:00'},
            {'nombre': 'Maratón de Barcelona', 'año': 2021, 'puesto': 3, 'tiempo': '2:20:00'}
        ]
    },
    '98765432B': {
        'nombre': 'Maria',
        'maratones': [
            {'nombre': 'Maratón de Sevilla', 'año': 2019, 'puesto': 2, 'tiempo': '2:10:00'},
            {'nombre': 'Maratón de Valencia', 'año': 2022, 'puesto': 1, 'tiempo': '2:05:00'}
        ]
    },
    # Otros maratonistas...
}

# Ordenar los maratonistas alfabéticamente
maratonistas_ordenados = sorted(maratonistas.items(), key=lambda x: x[1]['nombre'])

# Ordenar las maratones de cada maratonista según el tiempo ascendente
for maratonista in maratonistas.values():
    maratonista['maratones'] = sorted(maratonista['maratones'], key=lambda x: x['tiempo'])

# Imprimir los maratonistas ordenados y sus maratones ordenadas por tiempo
for dni, datos in maratonistas_ordenados:
    print(f"Maratonista: {datos['nombre']} (DNI: {dni})")
    print("Maratones:")
    for maraton in datos['maratones']:
        print(f"- {maraton['nombre']} ({maraton['año']}), Puesto: {maraton['puesto']}, Tiempo: {maraton['tiempo']}")
    print()


#Preguntar en el taller