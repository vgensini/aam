
# coding: utf-8

# ## Compute Global Atmospheric Relative Angular Momentum from CFSR Data
# ###### Inputs: 0.5 deg lat/lon grib2 data obtained from CFS Reanalysis (CFSR); need u-wind at all pressure levels 1000-1 hPa			
# ###### Outputs: Global Relative Atmospheric Angular Momentum  with units:
# $$kg \cdot m^2 \cdot s^{-1}$$
# ##### Created by: Dr. Victor Gensini (Fall 2016) | weather.cod.edu/~vgensini								

# In[140]:

#Import neccessary Python libraries (this example uses Python 2.7)
import numpy as np
import math, pygrib, datetime
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
from netCDF4 import Dataset, num2date
import os
import multiprocessing
years = np.arange(1979,2011,1)

def cat_nc(year):
	months = np.arange(1,13,1)
	for mn in months:
                print mn
		nc = Dataset(str(year)+'%02d'%(mn)+'_aam.nc','r')
		aam = nc.variables['aam'][:]
		time = nc.variables['time']
                tunits = time.units
                times = time[:]
		#times = num2date(time[:],units=time.units)
		lats = nc.variables['lats'][:]

                outfile = '%s_aam.nc'%year
                if os.path.isfile(outfile) == False:
                  ncfile = Dataset(outfile,'w',format='NETCDF4_CLASSIC')
                  ncfile.createDimension('time',None)
                  ncfile.createDimension('lat',len(lats))
                 
                  tim = ncfile.createVariable('time','d',('time',))
                  latitude = ncfile.createVariable('lats','d',('lat',))
                  aamvar = ncfile.createVariable('aam','d',('time','lat'))

                  tim[:] = times
                  tim.units = tunits
                  latitude[:] = lats
                  aamvar[:] = aam

                  ncfile.close()
                else:
                  ncfile = Dataset(outfile,'a',format='NETCDF4_CLASSIC')
                  appendtime = ncfile.variables['time']
                  appendvar = ncfile.variables['aam']
                  lentime = len(appendtime[:])
                  print lentime,len(times) 
                  appendtime[lentime:lentime+len(times)] = times
                  appendvar[lentime:lentime+len(times),:] = aam

                  ncfile.close()


numprocs=multiprocessing.cpu_count()
pool=multiprocessing.Pool(processes=numprocs)
r2=pool.map(cat_nc,years)
pool.close()

#cat_nc(1979)
#plt.pcolormesh(tiime,lats,aam.T)
#plt.title(r"$M_R$" ' by Latitude for ' +str(date.month)+'-'+str(date.day)+'-'+str(date.year)+' '+str(date.hour)+'Z') #Make a title
#plt.xlabel(r"$\phi$") #Label x-axis
#plt.ylabel(r"$kg \cdot m^2 \cdot s^{-1}$") #Label y-axis
#pqlt.xlim(-90,90) #Set limits on the x-axis
#plqt.xticks(np.arange(-90,110,20)) #Set x-axis ticks every 20 deg
#plt.tight_layout() #Make a nice layout
#bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.7)
#plt.annotate('Total AMM = '+'{:e}'.format(np.sum(aam)),xycoords='figure fraction', xytext=(.8,0.95),xy=(.8,0.95), textcoords='axes fraction',ha="center", va="center", size=8,bbox=bbox_props) #Annotate total AAM on the plot
#plt.savefig('test.png') #Display the plot
