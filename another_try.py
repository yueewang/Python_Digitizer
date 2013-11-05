# 2-D plot function for SODA TEMPERATURE 
# YUE WANG
# OCT. 31st 2013
import numpy as np
from datetime import datetime
import netCDF4 
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap,cm
import matplotlib.pyplot as plt 

#
class soda_animation(object):
    def model_visualization(self,url, llat=23., ulat=51., llon=-130., rlon=-65.):
        self.nc = Dataset(url)
        self.lon = self.nc.variables['LON'][:]
        self.lat = self.nc.variables['LAT'][:]
    #depth = nc.variables['DEPTH'][:]
        self.temp = self.nc.variables['TEMP'][:]
    #salt = nc.variables['SALT'][:]
    #u = nc.variables['U'][:]
    #v = nc.variables['V'][:]
    #w = nc.variables['W'][:]
    #taux = nc.variables['TAUX'][:]
    #tauy = nc.variables['TAUY'][:]
    #ssh = nc.variables['SSH'][:]
    
    #return lat,lon,temp
    #depth,temp,salt,u,v,w,taux,tauy,ssh

        self.m = Basemap(projection='robin',
                llcrnrlat=llat,
                urcrnrlat=ulat,
                llcrnrlon=llon+1,
                urcrnrlon=rlon-1,
                lon_0 =180,
                resolution='i')              

# Function Calls
#url = 'http://sodaserver.tamu.edu:80/opendap/SODA_2.2.8/ENSEMBLE_MEAN/SODA_2.2.8_187101.cdf'
#lat, lon, temp = model_visualization(url)

    def soda_temp_plot(self,nc,time,depth):
        
    
    
        fig = plt.figure(figsize=(20,10))
        ax = fig.add_axes([0.1,0.1,0.8,0.8])

        self.temp_0 = self.temp[time,depth,:,:]
    
        dates=netCDF4.num2date(self.nc.variables['TIME1'][:],\
        'seconds since 1916-01-02 12:00:00')
        DEPTH = nc.variables['DEPTH1_4']


            
        parallels = np.arange(-5.,5.,2.)
        self.m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
        meridians = np.arange(120.,300.,30.)
        self.m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

        ny = self.temp_0.shape[0]; nx =self.temp_0.shape[1]
        lons, lats = self.m.makegrid(nx, ny)
        x, y = self.m(lons, lats)
    
        self.cs = self.m.contourf(x,y,self.temp_0,cmap=cm.sstanom)
        self.m.drawcoastlines()
    
        cbar = self.m.colorbar(self.cs,location='bottom', size="15%", pad='35%')
        cbar.set_label('Temperature(deg.C)')
        ax.set_title('Sea Temperature at ' +str(dates[time])+ 'at depth of'+ str(DEPTH[depth])+' m')
        plt.show()