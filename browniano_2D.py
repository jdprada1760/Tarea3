import numpy as np
import matplotlib.pyplot as plt
import sys, string, os

n = int(sys.argv[1])
d = np.zeros(n+1)
actual = np.zeros(3)
for i in range(1, n+1):
    x = 1 - 2*np.random.random(1)
    y = 1 - 2*np.random.random(1)
    z = 1 - 2*np.random.random(1)
    a = np.sqrt(x**2 + y**2 + z**2)
    x = x/a
    y = y/a
    z = z/a
    actual[0] += x
    actual[1] += y
    actual[2] += z
    d[i] = np.sqrt(actual[0]**2 + actual[1]**2 + actual[2]**2)

e = range(n+1)
fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("Numero de pasos")
ax.set_ylabel("Distancia del origen")
ax.set_title("Movimiento Browniano")
ax.legend()
ax.plot(e, d, 'r', zorder=1, lw=1)
filename = 'browniano_2D_n'
plt.savefig(filename + '.pdf',format = 'pdf', transparent=True)
plt.close()

