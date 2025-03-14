import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interpn

x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
x1, y1 = np.meshgrid(x,y, indexing='ij')

r = np.sqrt(x1**2 + y1**2)
tetha = np.arctan2( y1, x1)
u = -r*np.sin(tetha)
v = r*np.cos(tetha)


dt = 0.01
xn = 0.3
yn = 1.6

print(x, end='\n'+40*'*')
print(y, end='\n'+40*'*')
print(u)
print(v)
plt.figure()
plt.quiver(x1, y1, u, v )
n=0
while n<700:
    plt.plot(xn, yn, '.', color=(1,0,0, 1))
    up = interpn((x,y), u, (xn,yn) )
    vp = interpn((x,y), v, (xn,yn) )
    
    xn = xn + dt*up
    yn = yn + dt*vp
    n += 1


plt.show()
