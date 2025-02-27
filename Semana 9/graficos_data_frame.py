import pandas as pd
import matplotlib.pyplot as plt

data = {'animal':['cat','snake','dog'],
        'age' : [2.5,3,7],
        'visits' : [1,3,2],
        'priority' : ['yes', 'yes', 'no']
    }

#Asignamos al data frame la info en este caso la varibale que contiene llamada (data)
df = pd.DataFrame(data)
df
print(df)

x_values = df['animal']
y_values = df['age']

fig , ax = plt.subplots()

ax.bar(x_values,y_values)

ax.set_xlabel("Animal")
ax.set_ylabel("Edad (Años)")

ax.set_title("Mascotas")

plt.show()


