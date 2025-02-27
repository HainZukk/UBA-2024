import csv

def transformar_csv_a_txt(input_csv, output_txt):
    with open(input_csv, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        
        with open(output_txt, mode='w', encoding='utf-8') as txtfile:
            for row in reader:
                nombre, color, le_gusta = row
                le_gusta_texto = "sí" if le_gusta.strip().lower() == "si" else "no"
                txtfile.write(f"A {nombre.strip()} {'sí' if le_gusta_texto == 'sí' else 'no'} le gusta el {color.strip()}\n")

# Uso de la función
transformar_csv_a_txt('gustos.csv', 'gustos.txt')
