#Importamos libreria 
import matplotlib.pyplot as plt

#Valores que se desean graficar 
x = [0,1,2,3,4,5]
y_linear = [0,1,2,3,4,5]        #grafica lineal
y_quadratic = [0,1,4,9,16,25]       #grafica cuadratica
y_cubic = [0,1,8,27,64,125]             #grafica cubica

fig , ax = plt.subplots(figsize = (5,3))       #Figsize establece el tamaño de la figura figsize(width , height)

#Establecemos ax.plot() de cada una con un label o referencia (Acordarme de diferencia de labels y label / plots y plot)
ax.plot(x, y_linear, label ='Lineal')
ax.plot(x, y_quadratic, label ='Cuadratica')
ax.plot(x, y_cubic, label = 'Cubico')

#Establcemos el titulo de la axe
ax.set_title("Grafico con multiples curvas")
ax.set_xlabel('X')      #Establcemos referncias por ejemplo del eje X 
ax.set_ylabel('Y')              #Lo mismo pero con el eje Y

# ax.legen() se utiliza para añadir una leyenda al gráfico. Una leyenda es una caja que 
# describe los elementos representados en el 
# gráfico, como líneas, barras, puntos, etc. Esta función es especialmente útil cuando tienes 
# múltiples conjuntos de datos o series en el mismo 
# gráfico y necesitas identificar claramente qué representa cada uno
ax.legend() 

#Mostramos la grafica
plt.show()


