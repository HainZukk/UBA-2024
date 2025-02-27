archive = open("personas.csv")
personas_crudo = archive.readlines()
archive.close

#Nos devuelve una lista de cadenas
#       print(personas_crudo)

def transformar(persona):
    persona = persona.strip("\n")
    persona = persona.split(";")
    return persona


personas = list(map(transformar, personas_crudo))

suma_edades = 0
for persona in personas:
    [nombre,edad] = persona
    suma_edades += int(edad)

print("el promedio de edad es " , suma_edades / len(personas))