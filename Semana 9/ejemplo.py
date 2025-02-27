import matplotlib.pyplot as plt
# Grafico elemental

x = [0,2,10,11,18,25]
y = [0,1,2,3,4,5]

fig, ax = plt.subplots()

#Referenciamos a label = "Objeto 1" modificamos color , tipo de marcador y tipo de linea etc.
ax.plot(x,y , label = 'Objeto 1', color = 'green' , marker = 'o' , linestyle = '--' , markersize = 8, linewidth = 1.2)

ax.set_title("Grafico de posicion")

ax.set_xlabel('Tiempo (min)')
ax.set_ylabel('Distancia (max)')

#Establecer limites de los ejes 
ax.set_xlim(0,30)
ax.set_ylim(0,6)

#Agregar la referencia
ax.legend()

#grilla prestablecida
ax.grid()
plt.show()