def promedio(notas):
    total = 0 
    cant_notas = 0
    for nota_estudiantes in notas:
        if (nota_estudiantes["intento"] == 1):      #Si el intento del estudiante es 1 suma a cant de notas 1
            cant_notas = cant_notas + 1
            total = total + nota_estudiantes["nota"]
    return total / cant_notas



        #Diccionario

notas = {
    "nombre" : "Liz",
    "apellido" : "Peralta",
    "intento" : 1 ,
    "nota" : 8
},
{
    "nombre" : "Uriel",
    "apellido" : "Garrott",
    "intento" : 1,
    "nota" : 7
},
{
    "nombre" : "Facundo",
    "apellido" : "Barrionuevo",
    "intento" : 1,
    "nota" : 3 
},
{
    "nombre" : "Natalia",
    "apellido" : "Pereira",
    "intento" : 2,
    "nota" : 4
}
print(promedio(notas))