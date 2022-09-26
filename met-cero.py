"""Copyright (c) 2022 Martina Contreras <mcontrerasp2021@udec.cl>
En este programa resolveremos f(x) = x -exp(-x) == 0
usando el metodo de la biseccion
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x - np.exp(-x)

#crear una lista de valores de x
x = np.linspace(0, 5, 100)

plt.plot(x, x)
plt.plot(x, np.exp(-x))
plt.show()