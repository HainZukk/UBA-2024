import matplotlib.pyplot as plt

#Establecemos listas con lo necesario para la receta
peso = [340 , 115 , 200 , 200 , 270]
ingredientes = ['chocolate','leche','manteca' ,'azucar' ,'harina']

#fig, ax = plt.subplots() crea una figura y un conjunto de ejes.
fig , ax = plt.subplots()       

#ax.bar() permite crear un grafico de barras 1ro recibe un arreglo con las etiquetas y luego otro arreglo con la altura de cada una
ax.barh(ingredientes , peso)

#Establecemos las etiqueta de los ax tanto eje Y como el eje X
ax.set_xlabel('Peso(Gr)')
ax.set_ylabel('Ingredientes')

#Establecemos el titulo del grafico o axe
ax.set_title("Receta en manera horizontal")

#Mostramos el grafico 
plt.show()