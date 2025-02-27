import csv

def guardar_notas(diccionarios_notas):
    # Nombres de los campos en el archivo CSV
    fieldnames = ['nombre', 'apellido', 'dni', 'nota']
    
    # Guardar las notas en el archivo CSV
    with open('notas.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Escribir el encabezado
        writer.writeheader()
        
        # Escribir cada diccionario en una fila del archivo CSV
        for nota in diccionarios_notas:
            writer.writerow(nota)

# Ejemplo de uso
notas = [
    {'nombre': 'Tobias', 'apellido': 'Nguyen', 'dni': '47526419', 'nota': 7},
    {'nombre': 'Vanesa', 'apellido': 'Yacanto', 'dni': '26180428', 'nota': 9},
    {'nombre': 'Liz', 'apellido': 'Peralta', 'dni': '47412389', 'nota': 9},
    {'nombre': 'Uriel', 'apellido': 'Garrott', 'dni': '47512321', 'nota': 6},


    # Otros diccionarios de notas...
]

guardar_notas(notas)