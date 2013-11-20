# 2-D plot function for SODA TEMPERATURE 
# YUE WANG
# Nov. 12st 2013
import numpy as np
import netCDF4 
from mpl_toolkits.basemap import Basemap,cm
import matplotlib.pyplot as plt 

def soda_plot(url,variable,llat, ulat, llon, rlon,time=3,depth=0):
    
    nc = netCDF4.Dataset(url)
    t  = time
    d  = depth
    dep = nc.variables['DEPTH1_3'][:]
    dates= netCDF4.num2date(nc.variables['TIME1'][:],\
        'seconds since 1916-01-02 12:00:00')
    
    var = nc.variables[variable][t,d,:,:]
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
    plt.title(str(variable)+' at Depth of '+str(dep[d])+' (m) ('+ str(dates[t])+')')
    plt.show()
    
    #plt.savefig('SST_globeplot_Hw3.png')


##########
url = 'http://sodaserver.tamu.edu:80/opendap/TEMP/SODA_2.3.1_01-01_python.cdf'
variable = 'TEMP'
llat = -5.
ulat = 5.
llon = 20.
rlon = 180.
soda_plot(url,variable,llat, ulat, llon, rlon,time=3,depth=0)