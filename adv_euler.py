import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interpn
import time_dif_sch as tds

#Ejercicio campo vectorial circular

#creando campo vectorial
x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
x1, y1 = np.meshgrid(x,y, indexing='ij')

r = np.sqrt(x1**2 + y1**2)
tetha = np.arctan2( y1, x1)
u = -r*np.sin(tetha)
v = r*np.cos(tetha)

dt = 0.01
# posición inicial
xn = 0.3
yn = 1.6

# Gráfico del campo de velocidades
plt.figure()
plt.quiver(x1, y1, u, v )
n=0

# Graficando posición con euler
while n<700:
    plt.plot(xn, yn, '.', color=(1,0,0, 1))
    xn, yn  = tds.euler_fw( x, y, u, v, (xn, yn), dt)
    n += 1


plt.show()
