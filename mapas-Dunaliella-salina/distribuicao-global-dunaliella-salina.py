#Mapa da Distribuição Global da Dunaliella salina (Dunal) Teodoresco
#Escrito por Andre Rossi Korol

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='robin', resolution = 'h', area_thresh = 1000.0,
              lat_0=0, lon_0=0)
map.drawcoastlines()
map.drawcountries()
#map.fillcontinents(color='white')
map.bluemarble()
map.drawmapboundary(fill_color='gray')
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30)) 

lons = [2.8577105, 34.299316, 10.451526, 24.96676, -3.74922, -16.6291304, 30.802498, 53.688046, 174.885971, 3.876716]
lats = [39.5341789, 43.413029, 51.165691, 45.943161, 40.463667, 28.2915637, 26.820553, 32.427908, -40.900557, 43.610769]
x,y = map(lons, lats)
map.plot(x, y, 'ro', markersize=12)

plt.show()	