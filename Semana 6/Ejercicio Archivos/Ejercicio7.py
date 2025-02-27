import csv

# Abrir y leer el contenido de los archivos
with open('salas.txt') as file:
    contenido1 = [line.strip() for line in file.readlines()]  # Leer todas las líneas y eliminar '\n'

with open('peliculas.txt') as file2:
    contenido2 = [line.strip() for line in file2.readlines()]  # Leer todas las líneas y eliminar '\n'

# Crear el objeto zip con el contenido leído
combinado = zip(contenido1, contenido2)

# Crear y escribir en el archivo CSV
with open('combinado.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for c in combinado:
        writer.writerow(c)

print("Archivo CSV creado exitosamente.")
