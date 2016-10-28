
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
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
start_input = '2006050100' #YYYYMMDDHH
end_input  =  '2006050100' #YYYYMMDDHH

begdate = datetime.datetime.strptime(start_input,"%Y%m%d%H")
enddate = datetime.datetime.strptime(end_input,"%Y%m%d%H")
dates = []
while begdate <= enddate:
        dates.append(begdate)
        begdate+=datetime.timedelta(days=1)

#Declare physical constants
pi = math.pi #Pi
rad = pi/180. #radians
gravity = 9.81 #gravitational acceleration ms^-2
earth_r = 6371220. #Earth's radius in (m)

#I've concatenated CFSR 6-hrly data into monthly chunks following a format of <cfsr_YYYYMM.grb2>
#data_file = '/home/vgensini/data/CFSR/cfsr_'+str(enddate.year)+str(enddate+relativedelta(months=-1).month)+'.grb2'
data_file = '/home/vgensini/data/CFSR/cfsr_200605.grb2'
gr = pygrib.open(data_file) #Read CFSR grib2 file containing u-winds at all pressure levels into memory
for date in dates:
	# ### Read in all U-component (i.e., zonal) wind values
	umsgs = gr.select(name='U component of wind',typeOfLevel='isobaricInhPa', year=date.year,month=date.month,day=date.day, hour=date.hour)
	lats,lons = umsgs[0].latlons() #Read the lat/lon information from the u-wind grib2 message
	uwnd = np.zeros((361, 720, 37)) #Could do some fancy dynamic shape finding here
	for i,levs in enumerate(umsgs): #CFSR 0.5 data is x-720,y-361,z-37
		uwnd[:,:,i] = levs.values   #Read zonal wind into a 3-D NumPy array
	dps=[0.,100.,200.,200.,300.,1000.,1000.,2000.,2000.,3000.,2500.,2500.,2500.,2500.,2500.,2500.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,0.]
	dps = np.tile(np.array(dps),(361,720,1)) #Create a 3-D NumPy array of dp values
	UDP = np.multiply(uwnd,dps) #Calculate UDP
	level_UDP = np.sum(UDP, axis=(2)) #Sum across all levels
	zonalavg_UDP = np.mean(level_UDP, axis=(1)) #Zonal mean across all longitudes
	dlat = 0.5 * rad #Latitude delta in radians (0.5 lat/lon grid spacing for this dataset)
	aam = zonalavg_UDP * np.cos(lats[:,0] * rad) * np.cos(lats[:,0] * rad) * dlat * 2.* pi * earth_r**3 / gravity #Calculate AAM
	aam.dump(date.strftime('%Y%m%d%H')+'aam.npy')
	#plt.plot(lats[:,0],aam) # plot latitude (x-axis) by global relative aam (y-axis)
plt.plot(lats[:,0],aam)
plt.title(r"$M_R$" ' by Latitude for ' +str(date.month)+'-'+str(date.day)+'-'+str(date.year)+' '+str(date.hour)+'Z') #Make a title
plt.xlabel(r"$\phi$") #Label x-axis
plt.ylabel(r"$kg \cdot m^2 \cdot s^{-1}$") #Label y-axis
plt.xlim(-90,90) #Set limits on the x-axis
plt.xticks(np.arange(-90,110,20)) #Set x-axis ticks every 20 deg
plt.tight_layout() #Make a nice layout
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.7)
plt.annotate('Total AMM = '+str(np.sum(aam)),xycoords='figure fraction', xytext=(.8,0.95),xy=(.8,0.95), textcoords='axes fraction',ha="center", va="center", size=8,bbox=bbox_props) #Annotate total AAM on the plot
plt.savefig('test.png') #Display the plot
