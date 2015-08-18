from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
map = Basemap(projection='ortho', lat_0=50, lon_0=-100,
              resolution='h', area_thresh=1000.0)
 
map.drawcoastlines()
map.drawcountries()

map.drawrivers()
map.shadedrelief()
plt.show()