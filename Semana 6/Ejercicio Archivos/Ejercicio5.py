def leer_mostrar_informacion(archivo_csv):
    with open(archivo_csv, 'r') as file:
        for line in file:
            # Mostrar la línea tal como está para identificar problemas
            print("Línea del archivo:", line)
            try:
                # Dividir la línea en sus componentes
                nombre, codigo, precio, stock = line.strip().split(',')
                # Mostrar en el formato especificado
                print(f"Nombre producto: {nombre}")
                print(f"Código producto: {codigo}")
                print(f"Precio por unidad: {precio}")
                print(f"Stock: {stock}\n")
            except ValueError:
                print("Error: La línea no tiene el formato esperado.")


import csv
def agregar_linea(archivo_csv, diccionario_linea):
    with open(archivo_csv, "a", newline='') as file:
        fieldnames = ['nombre', 'codigo', 'precio', 'stock']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(diccionario_linea)

linea = {
    "nombre" : "hojas a4",
    "codigo" : "35662",
    "precio" : 600,
    "stock" : 45
}
# Ejemplo de uso
leer_mostrar_informacion("archivo5.csv")
agregar_linea("archivo5.csv" , linea)
