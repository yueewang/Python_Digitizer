# 2-D plot function for SODA TEMPERATURE 
# YUE WANG
# Nov. 12st 2013
import numpy as np
import netCDF4 
from mpl_toolkits.basemap import Basemap,cm
import matplotlib.pyplot as plt 

def soda_plot(url,variable,llat, ulat, llon, rlon,time,depth):
    
    nc = netCDF4.Dataset(url)
    t  = time
    d  = depth
    var = nc.variables[variable][t,d,:,:]
#Q: do we need define t,d in function
    lon = nc.variables['LON'][:]
    lat = nc.variables['LAT'][:]

    # setting up data into basemap with given projection 
    lons, lats = np.meshgrid(lon, lat)
    fig = plt.figure(figsize=(16,8))
    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    m = Basemap(llcrnrlat=llat,urcrnrlat=ulat,\
            llcrnrlon=llon,urcrnrlon=rlon,\
            projection='mill',resolution = 'h',ax=ax)
    x,y = m(lons, lats)            

    # drawing the map
    m.fillcontinents(color='gray',lake_color='gray')
    m.drawcoastlines(linewidth = 0.4)
    m.drawparallels(np.arange(-90.,90.,15.), labels =[1,0,0,1],fontsize=10)
    m.drawmeridians(np.arange(-180.,181.,40.),labels =[0,1,0,1],fontsize=10)
    m.drawmapboundary()

    # plotting data on the map 
    plt.contourf(x,y,var,cmap=cm.sstanom)
    cb = plt.colorbar(orientation='horizontal')
    cb.set_label(r'Sea Surface Temperature (deg C)',fontsize=14,style='italic')
    plt.show()
    #plt.savefig('SST_globeplot_Hw3.png')
## Do I need a title for the plot or a title for the whole plot?



'''url = 'http://sodaserver.tamu.edu:80/opendap/TEMP/SODA_2.3.1_01-01_python.cdf'
variable = 'TEMP'
#nino 3.4 region
llat = -5.
####Q: range of latitude: 0-360, do we need a loop? transfore the latidue
ulat = 5.
llon = -170.
rlon = -120.'''