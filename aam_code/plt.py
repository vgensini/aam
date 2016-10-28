
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
start_input = '2006050100' #YYYYMMDDHH
end_input  =  '2006053100' #YYYYMMDDHH

begdate = datetime.datetime.strptime(start_input,"%Y%m%d%H")
enddate = datetime.datetime.strptime(end_input,"%Y%m%d%H")
dates = []
while begdate <= enddate:
        dates.append(begdate)
        begdate+=datetime.timedelta(days=1)
aamf = np.zeros((361))
for dt in dates:
	aam=np.load(dt.strftime('%Y%m%d%H')+'aam.npy')
	aamf = np.column_stack((aamf,aam))
	print aamf.shape
plt.pcolormesh(np.arange(0,32,1),np.arange(-90,90.5,.5),aamf)
#plt.title(r"$M_R$" ' by Latitude for ' +str(date.month)+'-'+str(date.day)+'-'+str(date.year)+' '+str(date.hour)+'Z') #Make a title
plt.xlabel(r"$\phi$") #Label x-axis
plt.ylabel(r"$kg \cdot m^2 \cdot s^{-1}$") #Label y-axis
#plt.xlim(-90,90) #Set limits on the x-axis
#plt.xticks(np.arange(-90,110,20)) #Set x-axis ticks every 20 deg
plt.tight_layout() #Make a nice layout
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.7)
plt.annotate('Total AMM = '+'{:e}'.format(np.sum(aam)),xycoords='figure fraction', xytext=(.8,0.95),xy=(.8,0.95), textcoords='axes fraction',ha="center", va="center", size=8,bbox=bbox_props) #Annotate total AAM on the plot
plt.savefig('test.png') #Display the plot

