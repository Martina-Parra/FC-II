import numpy as np
import matplotlib.pyplot as plt
 
h = np.geomspace(1, 1e-20, 300)
x = 1.4
eps = 2**(-52)
df = ( np.sin(x+h) - np.sin(x) ) / h
df_an = np.cos(x)

error_num = np.abs( df_an - df)
error_an = 0.5*h*abs( np.sin(x) ) + 2*eps*np.abs( np.sin(x) ) /h
i = np.argmin(error_num)
h[i]

