from math import log

G = 1e-3
D = 2.52
gamma = 1.5

x_0 = 100
y_0 = 100

scale_factor = 1e5

L_micro = G
L_macro = scale_factor*G

n_0 = round( -log(L_macro)/log(gamma) )
n_inf = round( -log(L_micro)/log(gamma) )

import roughfrac as rf

test_fun = rf.weierstrass_mandelbrot(G, D, gamma, n_0, n_inf, x_0, y_0)
test_fun.print()

import numpy as np

Nx = 2000
Ny = 2000
x = np.linspace(0, L_macro, num=Nx)
y = np.linspace(0, L_macro, num=Ny)
Z = test_fun.evaluate_2D(x, y)

# TEST
print(Z.dtype)

X, Y = np.meshgrid(x, y)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
plt.show()
