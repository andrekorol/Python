#Code to read and plot earthquakes from the last 24 hours 
#Written by: Andre Rossi Korol

# --- Process Data ---

#First of all, you need to download the latest file that contains the data of the earthquakes that happened over the last 24 hours.
#You can download it at the USGS(United States Geological Survey) website: http://earthquake.usgs.gov/earthquakes/map/
#Make sure to download the file on the CSV file format, and to move it to a folder in your Desktop called 'datasets'
data_file = open('datasets/2.5_day(1).csv')
 
lats, lons = [], []
magnitudes = []
timestrings = []
for index, line in enumerate(data_file.readlines()):
    if index > 0:
        lats.append(float(line.split(',')[1]))
        lons.append(float(line.split(',')[2]))
        magnitudes.append(float(line.split(',')[4]))
        timestrings.append(' '.join(line.split(',')[0:1]).strip('"'))
 
# --- Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
map.drawcoastlines()
map.drawcountries()
#map.fillcontinents(color='white')
map.bluemarble()
map.drawmapboundary(fill_color='gray')
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
min_marker_size = 2.7
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = map(lon, lat)
    msize = mag * min_marker_size
    marker_string = get_marker_color(mag)
    map.plot(x, y, marker_string, markersize=msize)

title_string = "Earthquakes of Magnitude 1.0 or Greater\n"
title_string += "%s through %s" % (timestrings[-1], timestrings[0])

plt.title(title_string)
 
plt.show()