from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='merc', lat_0=-23.001388888889, lon_0=-43.358611111111,
 resolution = 'h', area_thresh = 0.01,
    llcrnrlon=-133.12498569488525, llcrnrlat=-66.51326044311185,
    urcrnrlon=60.234389305114746, urcrnrlat=25.79989118208833)	

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary(fill_color='royalblue')
#map.fillcontinents(color='forestgreen',lake_color='blue')
map.bluemarble()

lons = [-43.358611111111]
lats = [-23.001388888889]
x,y = map(lons, lats)
map.plot(x, y, 'ro', markersize=8)


plt.show()