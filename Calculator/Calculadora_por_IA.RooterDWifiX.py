import numpy as np

import tensorflow as tf

#Se define la red

capa1 = tf.keras.layers.Dense(units = 4, input_shape = [2])

#capa2 = tf.keras.layers.Dense(units = 4)

salida = tf.keras.layers.Dense(units = 1)

modelo = tf.keras.Sequential([capa1, salida])

modelo.compile(

    optimizer=tf.keras.optimizers.Adam(0.1),

    loss = 'mean_squared_error'

)

#Se define la forma del menú 

opciones = ["Nuevo"]

topologia = []

k = [1, 2, 3, 4]

#Se define el menú 

def f(w):

 for x in opciones:

     print(str(w) + ". " + x)

     w = w + 1

     s = int(input("Elije crack: "))

 if(s == 1):

     s_1 = input("Que nombre?: ")

     opciones.append(s_1)

     f(1)

 else:

      if(topologia.count(s) == 0):

          topologia.append(s)

          n = int(input("Cuantos datos de entrenamiento?: "))

          x = np.zeros([n, 2])

          y = np.zeros(n)

          m = 0

          while m < n:

              #adquirir datos

              a = float(input("Introduce un numero: "))

              b = float(input("Introduce otro: "))

              c = float(input("Introduce el resultado: "))

              x[m][0] = a

              x[m][1] = b

              y[m] = c

              m = m + 1

          print(x)

          print(y)

          print("Iniciando...")

          #entrenamiento

          historial = modelo.fit(x, y, epochs = 8000, verbose = False)

          print("Listo.")

          k[s] = modelo

          a = float(input("Introduce el 1er #: "))

          b = float(input("Introduce el 2do #: "))

          c = k[s].predict([[a, b]])

          print("El resultado es: ")

          print(c)

          f(1)

      else: 

        a = float(input("Introduce el 1er #: "))

        b = float(input("Introduce el 2do #: "))

        c = k[s].predict([[a, b]])

        print("El resultado es: ")

        print(c)

        f(1)

#Se llama a la función menú al iniciar el código 

f(1)

#Si sabes leerlo, puedes saltarte la introduccion de valores usando estos vectores que prepare :)

x = np.array([[1., 1.], [5., 5.], [5., 4.], [7., 3.], [2., 3.], [7., 2.], [1., 7.], [1, 3], [3, 1], [4, 5], [3, 6], [3, 5], [2, 4], [4, 2], [8, 2], [1, 0], [0, 1], [2, 0], [0, 2], [1, 2]])

y = np.array([ 2., 10.,  9., 10.,  5.,  9.,  8, 4, 4, 9, 9, 8, 6, 6, 10, 1, 1, 2, 2, 3])

#Para operaciones no lineales se debe introducir una funcion de activacion y habilitar la capa oculta desactivada, recomiendo una sigmoide. ergo no puedes sacar logaritmos, por ejemplo.
