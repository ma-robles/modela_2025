from netCDF4 import Dataset
from matplotlib import pyplot as plt
import cartopy.crs as ccrs
from scipy.interpolate import interpn
import numpy as np

from sys import argv

filename = argv[1]
print(filename)
root=Dataset(filename, 'r')

#lee datos
lat = root.variables['XLAT'][0,:]
lon = root.variables['XLONG'][0,:]
latu = root.variables['XLAT_U'][0,:]
lonu = root.variables['XLONG_U'][0,:]
latv = root.variables['XLAT_V'][0,:]
lonv = root.variables['XLONG_V'][0,:]

# tomando el nivel 5
level = 5
U = root.variables['U'][:, level][:]
V = root.variables['V'][:, level][:]

print('u',U.shape)

t = 10
# interpolando a malla escalar
def inter_esc( UV, latuv, lonuv, lat, lon, t):
    lonlat =  np.stack([ np.ravel(lat) , np.ravel(lon)], axis=1)
    UV_inter= np.reshape(
            interpn( (latuv.T[t],lonuv[t]),
                UV[t],
                lonlat,
                ),
            lat.shape,
         )
    return UV_inter

Ut = inter_esc(U, latu, lonu, lat, lon, t)
Vt = inter_esc(V, latv, lonv, lat, lon, t)

#coordenadas Popo
Xpopo = 19.021
Ypopo = -98.627

#obtiene limites
latmin = lat[0, 0]
latmax = lat[-1, 0]
lonmin = lon[0, 0]
lonmax = lon[0, -1]

plt.ion()
proj = ccrs.PlateCarree()
ax_lim= [lonmin, lonmax, latmin, latmax]
fig = plt.figure()
t=0
levels = range(0, 60,5)
while t < U.shape[0]:
    Ut = inter_esc(U, latu, lonu, lat, lon, t)
    Vt = inter_esc(V, latv, lonv, lat, lon, t)
    ax = plt.axes(projection= proj)
    ax.set_extent(ax_lim, proj)
    #dibuja grid
    ax.gridlines(draw_labels=["top", "right"], 
            dms=True, 
            x_inline=False, 
            y_inline=False,
            )
    #dibuja lineas de costa
    ax.coastlines()
    # graficacion de variable
    var_map = plt.contourf(lon, lat, np.sqrt(Ut**2+Vt**2),
           levels,
           transform= proj,
           )

    #color bar
    cbar=plt.colorbar(
           var_map,
           #ax=ax,
           #shrink=0.75,
           orientation='horizontal',
           aspect=50,
           pad=0.02,
           fraction=0.03,
           )
    cbar.ax.set_xlabel('tiempo ' + str(t))
    plt.show()
    plt.pause(0.2)
    plt.clf()
    t+=1
    

#plt.savefig('figure_nc.png')
