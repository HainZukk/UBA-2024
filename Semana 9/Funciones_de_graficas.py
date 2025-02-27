import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
x_linear = [0, 1, 2, 3, 4, 5]        # Grafica lineal
x_quadratic = [0, 1, 4, 9, 16, 25]    # Grafica cuadratica
x_cubic = [0, 1, 8, 27, 64, 125]

def create_easy_graph(x, y, label, ax, xlabel, ylabel, title, color=None):
    if color is None:
        color = "blue"
    # Definir el gráfico
    ax.plot(x, y, label=label, color=color)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    return ax

fig, ax = plt.subplots(3)

create_easy_graph(x, x_linear, "x", ax[0], "Eje X", "Eje Y", "Lineal", color="green")
create_easy_graph(x , x_quadratic , "x" , ax[1] , "Eje X" , "Eje Y" ,"Cuadratica" , color="blue" )
create_easy_graph(x, x_cubic , "x" , ax[2],"Eje X" , "Eje Y" , "Cuadratica" , color="red")

for axes in ax[:]:
    axes.grid()
    axes.legend()

plt.show()

