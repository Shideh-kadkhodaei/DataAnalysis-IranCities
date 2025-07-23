from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# create new figure, axes instances.
fig=plt.figure(figsize=(10, 8))
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
m = Basemap(llcrnrlon=40.,llcrnrlat=20.,urcrnrlon=70.,urcrnrlat=45.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=40.,lon_0=-20.,lat_ts=20.)

m.drawcoastlines()
m.fillcontinents()
m.drawcountries()
m.drawcounties()
m.drawstates()

Cities = ['Tehran', 'Shiraz', 'Mashhad', 'Isfahan', 'Tabriz', 'Qom', 'Ahvaz', 'Kermanshah', 'Karaj', 'Urmia']
lon = [51.2323, 52.3233, 59.3236, 51.4013, 46.1757, 50.5235, 48.4042, 47.0528, 50.5803, 45.0353]  #X
lat = [35.4120, 29.3636, 36.19435, 32.3955, 38.0454, 34.3824, 31.1817, 34.2013, 35.4945, 37.3238]  #y
population = [168, 20, 35, 22, 17, 13, 13, 10, 16, 7.3]    #s

colors = ['red', 'green', 'blue', 'orange', 'purple', 'magenta', 'maroon', 'yellow', 'black', 'brown']

X,y = m(lon,lat)
m.scatter(X,y,s=population, color=colors)

legend_x = 0.72
legend_y_start = 0.9
dy = 0.035
 
legend_patches = [ ]
for i in range(len(Cities)):
    patch = mpatches.Patch(color=colors[i], label=Cities[i])
    legend_patches.append(patch)
plt.legend(handles=legend_patches, loc='upper left', bbox_to_anchor=(1, 0.5), title='Cities')

ax.set_title('Top 10 Most Populous Cities in Iran')
plt.show()
