import csv
def contar_alumnos_aprobados(archivo_csv):
    #contar alumnos aprobados
    contador = 0
    with open(archivo_csv, "r") as file:
        leer_archivo = csv.DictReader(file)
        for x in leer_archivo:
            nota = int(x['nota'])
            if nota > 4:
                contador += 1
    return contador

cantidad_aprobados = contar_alumnos_aprobados('notas.csv')
print(f'La cantidad de aprobados son : {cantidad_aprobados}')