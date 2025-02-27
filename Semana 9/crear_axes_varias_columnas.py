import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
x_lineal = [0,1,2,3,4,5]
x_cuadratic = [0,1.4,9,16,25,6]
x_cubic = [0,1,8,27,64,125]

fig , ax = plt.subplots(nrows=3, ncols=3)

fig.subplots_adjust(wspace= 0.5 , hspace= 0.5)

ax[0,0].plot(x,x_lineal)
ax[0,1].plot(x,x_cuadratic) 
ax[0,2].plot(x,x_cubic)

plt.show()