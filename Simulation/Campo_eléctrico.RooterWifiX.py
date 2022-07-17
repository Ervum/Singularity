import numpy as np

import numba

from numba import jit

import matplotlib.pyplot as plt

import matplotlib.animation as animation

r = 3

e0 = 8.85*(10**(-12))

N = 10

pi = np.pi

theta = np.linspace(0, 2*pi, 1000)

thet = np.linspace(0,2*pi, 32)

PHI, THETA = np.meshgrid(thet, thet)

x = np.linspace(-4, 4, N)

y = np.linspace(-4, 4, N)

z = np.linspace(-4, 4, N)

lam = 1

la = (lam*r)/(4*pi*e0) 

X, Y, Z = np.meshgrid(x, y, z)

Ex = X + Y + Z

Ey = X + Y + Z

Ez = X + Y + Z

#Se resuelven las ecuaciones integrales para las componentes del campo eléctrico 

for i in range(N):

  for j in range(N):

    for k in range(N):

     Ex[i][j][k] = -1*np.trapz(( (r*np.cos(theta) - x[i])/(   ( (r*np.cos(theta)-x[i])**2 + (r*np.sin(theta)-y[j])**2 + z[k]**2)**(3/2)  )), theta)

     Ey[i][j][k] = -1*np.trapz(( (r*np.sin(theta) - y[j])/(   ( (r*np.cos(theta)-x[i])**2 + (r*np.sin(theta)-y[j])**2 + z[k]**2)**(3/2)  )), theta)

     Ez[i][j][k] = -1*np.trapz(( (- z[k])/(   ( (r*np.cos(theta)-x[i])**2 + (r*np.sin(theta)-y[j])**2 + z[k]**2)**(3/2)  )), theta)

#Plot

print(la*np.trapz(( (r*np.cos(theta) - 1)/(   ( (r*np.cos(theta)-1)**2 + (r*np.sin(theta)-4)**2)**(3/2)  )), theta))

print(la*np.trapz(( (r*np.cos(theta) + 1)/(   ( (r*np.cos(theta)+1)**2 + (r*np.sin(theta)+4)**2)**(3/2)  )), theta))

ax = plt.figure().add_subplot(projection="3d")

ax.quiver(X, Y, Z, Ex, Ey, Ez)

X = (3 + 0.25*np.cos(PHI))*np.cos(THETA)

Y = (3 + 0.25*np.cos(PHI))*np.sin(THETA)

Z = 0.25*np.sin(PHI)

ax.plot_surface(X, Y, Z)

plt.show()
