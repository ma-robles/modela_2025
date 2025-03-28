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
U = root.variables['U'][:,5][:]
V = root.variables['V'][:,5][:]

# interpolando a malla escalar
lonlat =  np.stack([ np.ravel(lat) , np.ravel(lon)], axis=1)
Ut = np.reshape(
        interpn( (latu.T[0],lonu[0]),
            U[0],
            lonlat,
            ),
        lat.shape,
     )

Vt = np.reshape(
        interpn( (latv.T[0],lonv[0]),
            V[0],
            lonlat,
            ),
        lat.shape,
     )

#coordenadas Popo
Xpopo = 19.021
Ypopo = -98.627

#obtiene limites
latmin = lat[0, 0]
latmax = lat[-1, 0]
lonmin = lon[0, 0]
lonmax = lon[0, -1]

proj = ccrs.PlateCarree()
plt.figure()
ax_lim= [lonmin, lonmax, latmin, latmax]
ax = plt.axes(projection= proj)
ax.set_extent(ax_lim, proj)
#dibuja grid
ax.gridlines(draw_labels=["top", "right"], dms=True, x_inline=False, y_inline=False)
#dibuja lineas de costa
ax.coastlines()
# graficacion de variable
var_map = plt.contourf(lon, lat, Ut, transform= proj )
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
cbar.ax.set_xlabel('Variable')

plt.savefig('figure_nc.png')
