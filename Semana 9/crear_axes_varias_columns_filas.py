#Importamos libreria 
import matplotlib.pyplot as plt

#Valores que se desean graficar 
x = [0,1,2,3,4,5]
x_lineal = [0,1,2,3,4,5]        #Grafica lineal
x_quadratic = [0,1,4,9,16,25]       #Grafica cuadratica
x_cubic = [0,1,8,27,64,125]                 #Grafica cubica

fig , ax = plt.subplots(nrows=3 , ncols=3)

fig.subplots_adjust(wspace=0.5 , hspace= 0.5) # Con esto indicamos el espacio libre entre plots

#AX[FILA,COLUMNA] ax[0,1]
ax[0,0].plot(x,x_lineal)            
ax[0,1].plot(x,x_quadratic)
ax[0,2].plot(x,x_cubic)

plt.show()