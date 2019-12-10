from math import log

G = 1e-3
D = 1.52
gamma = 1.5

x_0 = 100

scale_factor = 1e5

L_micro = G
L_macro = scale_factor*G

n_0 = round( -log(L_macro)/log(gamma) )
n_inf = round( -log(L_micro)/log(gamma) )

import roughfrac as rf

test_fun = rf.weierstrass_mandelbrot(G, D, gamma, n_0, n_inf, x_0)
test_fun.print()

import numpy as np

Nx = 5000
x = np.linspace(0, L_macro, num=Nx)
y = test_fun.evaluate_1D(x)

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()

S_hat = test_fun.compute_structure_function()

# Power law (+/- constant C)
S = x**(4-2*D)

Nlog = 100
plt.loglog(x[0:Nlog], S[0:Nlog], 'b-', x[0:Nlog], S_hat[0:Nlog], 'r-')
plt.show()
