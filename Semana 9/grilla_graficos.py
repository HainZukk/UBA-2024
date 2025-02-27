#Importamos libreria 
import matplotlib.pyplot as plt

#Valores que se desean graficar 
x = [0,1,2,3,4,5]
x_linear = [0,1,2,3,4,5]        #grafica lineal
x_quadratic = [0,1,4,9,16,25]       #grafica cuadratica
x_cubic = [0,1,8,27,64,125]             #grafica cubica

fig , ax = plt.subplots(nrows=3 , ncols= 1)  # o simplemnte plt.subplots(1,2)

 #Indicamos la posicion de los axes con los numeros dentro de los []
ax[0].plot(x,x_linear)
ax[0].set_title("Lineal")

ax[1].plot(x,x_quadratic)
ax[1].set_title("Cuadratica")

ax[2].plot(x,x_cubic)      
ax[2].set_title("Cubico")

plt.show()



