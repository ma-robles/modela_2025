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
    k1x = dt* interpn( (x, y), u, p)
    k1y = dt* interpn( (x, y), v, p)
    pt = (p[0] + k1x, p[1] + k1y )
    k2x = dt* interpn( (x, y), u, pt)
    k2y = dt* interpn( (x, y), v, pt)

    xn = p[0] + (k1x + k2x)/2
    yn = p[1] + (k1y + k2y)/2
    return (xn, yn)




