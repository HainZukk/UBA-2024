#Importamos la libraria 

import matplotlib.pyplot as plt

#Cargamos las listas
peso = [340 , 115 , 200 , 200 , 270]
ingredientes = ['chocolate','leche','manteca' ,'azucar' ,'harina']

#Cargamos la figura y el axe
fig , ax = plt.subplots()

#Para crear graficos de torta debemos utilizar la funcion ax.pie()
        #autopct indica como se mostrara el porcentaje 
ax.pie(peso , labels = ingredientes , autopct = '%1.1f%%')

#Establecemos titulo
ax.set_title('Receta')

#Mostramos grafico
plt.show()