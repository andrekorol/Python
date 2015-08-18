from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='merc', lat_0=-23.80, lon_0=-46.02,
 resolution = 'h', area_thresh = 0.01,
    llcrnrlon=-46.06, llcrnrlat=-23.84,
    urcrnrlon=-45.96, urcrnrlat=-23.78)	

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')

plt.show()	