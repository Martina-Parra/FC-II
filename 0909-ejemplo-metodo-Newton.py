"""Copyright (c) 2022 Martina Contreras <mcontrerasp2021@udec.cl>
En este programa resolveremos f(x) = x - exp(-x) == 0
usando el metodo de Newton.
Nota: no se optiene el valor exacto, solo aproximaciones.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

def f(x):
    return x - np.exp(-x)

def df(x):
    """derivada de f(x)"""
    return 1 + np.exp(-x)

#Sea x una lista de valores.
x = np.linspace(0, 10, 100)  


#La siguiente gráfica, nos muestra la intersección de una recta y una curva. 

plt.plot(x, f(x))
plt.hlines(0.0, 0, 10, colors= "red") 

#Queremos encontrar en que punto (x,y) se poduce dicha intersección.


#metodo de newton
x0 = 10 # valor semilla o inicial
x1 = 1

tolerancia = 1e-5 #valor más cercano a 0
error = 1.0



while not np.abs(error)<tolerancia:
    error= f(x0)*(x1-x0)/(f(x1)-f(x0))
    x0, x1 = x1, x0-error
    # print(x1)


#asumimos que el ultimo valor de x1 es solucion de f(x1)=0
# plt.plot(x1, f(np.array(x1)), "o")
# plt.show() 



