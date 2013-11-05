# 2-D plot function for SODA TEMPERATURE 
# YUE WANG
# OCT. 31st 2013
import numpy as np
from datetime import datetime
import netCDF4 
from mpl_toolkits.basemap import Basemap,cm
import matplotlib.pyplot as plt 

def soda_temp_plot(file_name,t,d):
    
    file = '/Users/yuewang/Documents/study/courses/OCVN689/project/'+ str(file_name)
    nc = netCDF4.Dataset(file)
    
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_axes([0.1,0.1,0.8,0.8])

    temp = nc.variables['TEMP']

    temp_0 = temp[t,d,:,:]

    lon = nc.variables['LON241_580'][:]
    lat = nc.variables['LAT142_161'][:]
    Time = nc.variables['TIME1']
    DEPTH = nc.variables['DEPTH1_4']


    m = Basemap(llcrnrlat=lat[0],urcrnrlat=lat[-1],\
            llcrnrlon=lon[0],urcrnrlon=lon[-1],\
            projection='mill',resolution = 'h',ax=ax)
            
    parallels = np.arange(-5.,5.,2.)
    m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

    meridians = np.arange(120.,300.,30.)
    m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

    ny = temp_0.shape[0]; nx =temp_0.shape[1]
    lons, lats = m.makegrid(nx, ny)

    lons, lats = m.makegrid(nx, ny)
    x, y = m(lons, lats)
    #clevs = [0,6,30,60,90,150,210,270,330,390,450,510,570,630,690,750,870,990,1010,1200]
    #clevs = [0,1,2.5,5,7.5,10,15,20,30,40,50,70,100,150,200,250,300,400,500,600,750]
    cs = m.contourf(x,y,temp_0,cmap=cm.sstanom)
    #cs = m.contourf(x,y,rainfall_annual)
    m.drawcoastlines()
    
    cbar = m.colorbar(cs,location='bottom', size="15%", pad='35%')
    cbar.set_label('Temperature(deg.C)')
    ax.set_title('Sea Temperature at ' +str(Time[t])+ 'at depth of'+ str(DEPTH[d])+' m')
    plt.show()