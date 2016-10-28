
# coding: utf-8

# ## Compute Global Atmospheric Relative Angular Momentum from CFSR Data
# ###### Inputs: 0.5 deg lat/lon grib2 data obtained from CFS Reanalysis (CFSR); need u-wind at all pressure levels 1000-1 hPa			
# ###### Outputs: Global Relative Atmospheric Angular Momentum  with units:
# $$kg \cdot m^2 \cdot s^{-1}$$
# ##### Created by: Dr. Victor Gensini (Fall 2016) | weather.cod.edu/~vgensini								

# In[140]:

#Import neccessary Python libraries (this example uses Python 2.7)
import numpy as np
import math, datetime, Nio, multiprocessing
import matplotlib.pyplot as plt
file = open("AAM_climo.txt", "w")


#years=np.arange(1979,1987,1)
#years=np.arange(1987,1995,1)
years=np.arange(1995,2003,1)
#years=np.arange(2003,2011,1)


#Declare physical constants
pi = math.pi #Pi
rad = pi/180. #radians
gravity = 9.81 #gravitational acceleration ms^-2
earth_r = 6371220. #Earth's radius in (m)
dlat = 0.5 * rad #Latitude delta in radians (0.5 lat/lon grid spacing for this dataset)
dps=[0.,100.,200.,200.,300.,1000.,1000.,2000.,2000.,3000.,2500.,2500.,2500.,2500.,2500.,2500.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,0.]
dps=np.rollaxis(np.tile(dps[:],(361,720,1)),2)
lats=np.arange(-90,90.5,0.5)
def get_mon_aam(year):
	month = '01'
	if month=='01' or month=='03' or month=='05' or month=='07' or month=='08' or month=='10' or month=='12':
		emon = '31'
	elif month=='04' or month=='06' or month=='09' or month=='11':
		emon = '30'
	elif month=='02':
		emon == '28'
	start_input = str(year)+month+'0100'    #YYYYMMDDHH
	end_input  =  str(year)+month+emon+'18' #YYYYMMDDHH
	begdate = datetime.datetime.strptime(start_input,"%Y%m%d%H")
	enddate = datetime.datetime.strptime(end_input,"%Y%m%d%H")
	dates = []
	while begdate <= enddate:
		dates.append(begdate)
		begdate+=datetime.timedelta(hours=6)
	data_file = '/home/vgensini/data/CFSR/cfsr_'+str(year)+str(month)+'.grb2'
	gr = Nio.open_file(data_file,'r')
	for i,dt in enumerate(dates):
		### Read in all U-component (i.e., zonal) wind values
		umsgs=gr.variables['UGRD_P0_L100_GLL0'][i][:][:][:]
		lats=np.array(gr.variables['lat_0'])
		UDP = np.multiply(umsgs,dps) #Calculate UDP
		level_UDP = np.sum(UDP, axis=(0)) #Sum across all levels
		zonalavg_UDP = np.mean(level_UDP, axis=(1)) #Zonal mean across all longitudes	
		aam = zonalavg_UDP*np.cos(lats*rad)*np.cos(lats*rad)*dlat*2.*pi*earth_r**3/gravity #Calculate AAM
		#file.write(dt.strftime('%Y-%m-%d-%H')+','+str(np.sum(aam)))
		print dt.strftime('%Y-%m-%d-%H')+','+str(np.sum(aam))
	gr.close()

numprocs=multiprocessing.cpu_count()
pool=multiprocessing.Pool(processes=numprocs)
r2=pool.map(get_mon_aam,years)
pool.close()
#aam.dump(date.strftime('%Y%m%d%H')+'aam.npy')
#plt.plot(lats[:,0],aam) # plot latitude (x-axis) by global relative aam (y-axis)
# plt.plot(lats[:,0],aam)
# plt.title(r"$M_R$" ' by Latitude for ' +str(date.month)+'-'+str(date.day)+'-'+str(date.year)+' '+str(date.hour)+'Z') #Make a title
# plt.xlabel(r"$\phi$") #Label x-axis
# plt.ylabel(r"$kg \cdot m^2 \cdot s^{-1}$") #Label y-axis
# plt.xlim(-90,90) #Set limits on the x-axis
# plt.xticks(np.arange(-90,110,20)) #Set x-axis ticks every 20 deg
# plt.tight_layout() #Make a nice layout
# bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.7)
# plt.annotate('Total AMM = '+'{:e}'.format(np.sum(aam)),xycoords='figure fraction', xytext=(.8,0.95),xy=(.8,0.95), textcoords='axes fraction',ha="center", va="center", size=8,bbox=bbox_props) #Annotate total AAM on the plot
# plt.savefig('test.png') #Display the plot
