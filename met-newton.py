
import numpy as np
import matplotlib.pyplot as plt

def df(x):
    return 1 + np.exp(-x)




#metodo de newton
x0 = 1.0 # semilla

for i in range(5):
    x0 = x0-df(x0)/df(x0)
    print(x0)

plt.plot(x0, df(x0), "o")
plt.show() 




#Metodo de la bisección
a = 0
b = 1

for i in range(10):
    c = 0.5*(a+b)

    condicion = f(a)*f(b)

    if condicion<0:
        b=c
    else:
        a=c