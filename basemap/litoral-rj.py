from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='merc', lat_0=-23.01, lon_0=-43.36,
 resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-45.35, llcrnrlat=-24.15,
    urcrnrlon=-38.53, urcrnrlat=-21.04)	

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')

plt.show()	