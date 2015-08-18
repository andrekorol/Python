from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='merc', lat_0=-22.024545601240327, lon_0=-43.95996104925871,
 resolution = 'h', area_thresh = 0.01,
    llcrnrlon=-48.68408214300871, llcrnrlat=-25.36388227274024,
    urcrnrlon=-36.40136729925871, urcrnrlat=-18.87510275035649)	

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')

lons = [-45.923041799999964, -43.24422089999996]
lats = [-23.2325753, -22.9317903]
x,y = map(lons, lats)
map.plot(x, y, 'ro', markersize=8)

#Se quiser mostrar os nomes em cima de seus respectivos pontos ao dar o zoom logo apos plotar,
#basta apagar os offsets.
labels = ['Casa-SJC', 'Casa-RJ']
x_offsets = [-30000, -30000]
y_offsets = [18000, -43000]

for label, xpt, ypt, x_offset, y_offset in zip(labels, x, y, x_offsets, y_offsets):
	plt.text(xpt+x_offset, ypt+y_offset, label)

plt.show()	