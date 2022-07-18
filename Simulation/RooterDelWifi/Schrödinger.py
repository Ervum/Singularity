import numpy as np

import numba

from numba import jit

import matplotlib.pyplot as plt

import matplotlib.animation as animation

N = 201

Nt = 10001

dx = 1/(N-1)

dy = 1/(N-1)

dt = 1e-7

x = np.linspace(0, 1, N)

y = np.linspace(0, 1, N)

X, Y = np.meshgrid(x, y)

PI = np.pi

psi0 = (2/1)* np.sin(2*PI*X) * np.sin(2*PI*Y)

V = 20000000*np.exp(- (X-0.5)**2 - (Y-0.5)**2)

psi = np.zeros([Nt, N, N])

psi[0] = psi0 

#Se resuelve la ecuación de Schrödinger 

@jit(nopython=True)

def go_fast(psi):

 for t in range(0, Nt - 1):

    for i in range(1, N - 1):

        for j in range(1, N - 1):

            psi[t + 1][i][j] = (-(psi[t][i + 1][j] - 2*psi[t][i][j] + psi[t][i - 1][j])/(2*dx**2) -(psi[t][i][j+1] - 2*psi[t][i][j] + psi[t][i][j-1])/(2*dy**2) + V[i][j]*psi[t][i][j])*(dt/1j) + psi[t][i][j]

    print(t)

 return psi

psi_numba = go_fast(psi.astype(complex))

fig = plt.figure()

ax = plt.gca()

def actualizar(i):

    ax.clear()

    plt.contourf(X, Y, psi_numba[i], levels = 200)

    plt.title(str(i))

    plt.xlim(0, 1)

    plt.ylim(0, 1)

ani = animation.FuncAnimation(fig, actualizar, range(300))

plt.show()
