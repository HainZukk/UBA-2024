def mifuncion():
  dinero = 0 
  archive = open("regalo2.txt","r")
  participantes = archive.readlines()
  for x in participantes:
    dinero = dinero + 1000
  archive.close()
  return dinero

contar_personas = open("regalo2.txt" , "r")
personas = contar_personas.readlines()
for i in personas:
  print(i)

esta_santi = open("regalo2.txt","a")
if "Santi\n" in personas:
    esta_santi.write("Tomi")

total = mifuncion()
print(f"En total Ale tiene para el cumple de sol ${total}")