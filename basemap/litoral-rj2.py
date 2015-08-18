from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='merc', lat_0=-23.03, lon_0=-43.99,
 resolution = 'h', area_thresh = 0.01,
    llcrnrlon=-44.32, llcrnrlat=-23.25,
    urcrnrlon=-43.55, urcrnrlat=-22.91)	

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')

plt.show()	