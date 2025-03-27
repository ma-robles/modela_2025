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
xn = [0.3]
yn = [1.6]
xn2 = [0.3]
yn2 = [1.6]
xn3 = [0.3]
yn3 = [1.6]
xn4 = [0.3]
yn4 = [1.6]

# Gráfico del campo de velocidades
plt.figure()
plt.quiver(x1, y1, u, v )
n=0

# tiempos
from time import time
times={}
times['e.01'] = 0
times['e.01'] = 0
times['rk.01'] = 0
times['rk.1'] = 0

# Graficando posición inicial
plt.plot(xn, yn, 'x', color=(1,0,0, 1))
nsteps= 628
while n< nsteps*10:
    n += 1
    xt, yt  = tds.euler_fw( x, y, u, v, (xn3[-1], yn3[-1]), dt/10)
    xn3.append(xt[0])
    yn3.append(yt[0])
    if n> nsteps:
        continue
    xt, yt  = tds.euler_fw( x, y, u, v, (xn[-1], yn[-1]), dt)
    xn.append(xt[0])
    yn.append(yt[0])
    {}xt, yt  = tds.rk2( x, y, u, v, (xn2[-1], yn2[-1]), dt)
    xn2.append(xt[0])
    yn2.append(yt[0])
    if n> nsteps/10:
        continue
    xt, yt  = tds.rk2( x, y, u, v, (xn4[-1], yn4[-1]), dt*10)
    xn4.append(xt[0])
    yn4.append(yt[0])

plt.scatter(xn3, yn3, color = 'b', marker= '2', label = 'euler, dt=0.001')
plt.scatter(xn, yn, color = 'r', marker= '+', label = 'euler, dt=0.01' ) 
plt.scatter(xn2, yn2, color = 'c', marker= '*', label = 'RK2, dt= 0.01' )
plt.scatter(xn4, yn4, color = 'y', marker= 'p', label = 'RK2, dt= 0.1' )
plt.legend( loc='upper right')

plt.show()
