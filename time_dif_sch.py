'''
time-difference schemes library
using interpn as function
'''

from scipy.interpolate import interpn

'''
- x,y  vectores que definen la malla
- p punto
- dt delta de tiempo
- u malla de valores en x
- v malla de valores en y
'''
# Euler-forward scheme 2D
def euler_fw( x, y, u, v , p,  dt):

    xn = p[0] + dt* interpn( (x, y), u, p)
    yn = p[1] + dt* interpn( (x, y), v, p)
    return (xn, yn)

#runge-Kutta second order
def rk2( x, y, u, v, p, dt):
    k1x, k1y = euler_fw( x, y, u, v, p, dt)
    k2x = 3*k1x*dt/4
    k2y = 3*k1y*dt/4

    xn = p[0] + dt* interpn( (x, y), u, (k2x,k2y))
    yn = p[1] + dt* interpn( (x, y), v, (k2x, k2y))
    return (xn, yn)




