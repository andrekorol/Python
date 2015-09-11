from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='merc', lat_0=-23.001388888889, lon_0=-43.358611111111,
 resolution = 'h', area_thresh = 0.01,
    llcrnrlon=-43.49132538540289, llcrnrlat=-23.05003921756029,
    urcrnrlon=-43.27297211391851, urcrnrlat=-22.95270290174115)	

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary(fill_color='royalblue')
map.fillcontinents(color='forestgreen',lake_color='blue')


lons = [-43.358611111111]
lats = [-23.001388888889]
x,y = map(lons, lats)
map.plot(x, y, 'ro', markersize=12)

labels = ['Referência de Nível(RN)-Estação 1034B', ]
x_offsets = [-300, ]
y_offsets = [250, ]

for label, xpt, ypt, x_offset, y_offset in zip(labels, x, y, x_offsets, y_offsets):
	plt.text(xpt+x_offset, ypt+y_offset, label)

plt.show()