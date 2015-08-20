#Code to read and plot earthquakes from the last 7 days
#Written by: Andre Rossi Korol

# --- Process Data ---
data_file = open('datasets/earthquake_data.csv')
 
lats, lons = [], []
magnitudes = []
timestrings = []
for index, line in enumerate(data_file.readlines()):
    if index > 0:
        lats.append(float(line.split(',')[6]))
        lons.append(float(line.split(',')[7]))
        magnitudes.append(float(line.split(',')[8]))
        timestrings.append(' '.join(line.split(',')[4:6]).strip('"'))
 
# --- Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
map.drawcoastlines()
map.drawcountries()
#map.fillcontinents(color = 'gray')
map.bluemarble()
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
 
def get_marker_color(magnitude):
    if magnitude < 3.0:
        return ('go')
    elif magnitude < 5.0:
        return ('yo')
    else:
        return ('ro')
 
# Variable size dots:
#  go through each lat, lon, plot it individually, calculating size dynamically
#  magnitude 1.0 = min dot size; larger quakes scaled by magnitude
min_marker_size = 4
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = map(lon, lat)
    msize = mag * min_marker_size
    marker_string = get_marker_color(mag)
    map.plot(x, y, marker_string, markersize=msize)
 
title_string = "Earthquakes of Magnitude 1.0 or Greater that happened over the last 7 days, by Andre Rossi Korol"

plt.title(title_string)
 
plt.show()