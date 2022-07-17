import numpy as np

import tensorflow as tf

#muestras

set_1 = np.array([100000,95000, 90000,85000, 80000,75000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000])/100000

set_2 = np.array([0.3,0.4, 0.5,0.52, 0.6,0.63, 0.7, 0.9, 1.2, 1.9, 2.5, 5, 10, 15, 20, 25, 30, 40, 60, 85])/85

#red

capa1 = tf.keras.layers.Dense(units = 4, input_shape = [1], activation = 'sigmoid')

capa2 = tf.keras.layers.Dense(units = 4, activation = 'sigmoid')

salida = tf.keras.layers.Dense(units = 1, activation = 'sigmoid')

modelo = tf.keras.Sequential([capa1, capa2, salida])

modelo.compile(

    optimizer=tf.keras.optimizers.Adam(0.1),

    loss = 'mean_squared_error'

)

print("Iniciando...")

#entrenamiento

historial = modelo.fit(set_1, set_2, epochs = 8000, verbose = False)

print("Listo.")

#Error

import matplotlib.pyplot as plt

#plt.xlabel = "Época"

#plt.ylabel = "Error"

#plt.scatter(set_2, set_1)

x = np.linspace(0, 100000, 100000)

y= modelo.predict([x/100000])*85

plt.plot(y, x)

plt.scatter(set_2*85, set_1*100000)
