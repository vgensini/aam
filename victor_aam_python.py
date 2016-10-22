#!/usr/bin/python2.7
#Victor's test program to calculate Earth's relative angular momentum
#####################################################################
import numpy as np
import math, pygrib
import matplotlib.pyplot as plt
#####################################################################
#CONSTANTS
pi = math.pi
rad = pi/180.
twopi = 2.*pi
gravity = 9.81
radius_E = 6371220.
radius_E3 = radius_E**3
######################################################################
#def earth_amm(U,DP,LAT,WGT)
gr = pygrib.open('/home/vgensini/data/CFSR/cfsr_199405.grb2')
pres = gr.select(name ='Pressure reduced to MSL')[0]
umsgs = gr.select(name='U component of wind',typeOfLevel='isobaricInhPa', year=1994,month=5,day=23, hour=0)
lats,lons = pres.latlons()
uwnd = np.zeros((361, 720, 37))
for i,levs in enumerate(umsgs):
	#print levs
	uwnd[:,:,i] = levs.values
#dps=[100.,100.,200.,200.,300.,1000.,1000.,2000.,2000.,3000.,2500.,2500.,2500.,2500.,2500.,2500.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,1300.]
dps=[0.,100.,200.,200.,300.,1000.,1000.,2000.,2000.,3000.,2500.,2500.,2500.,2500.,2500.,2500.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,0.]
dps = np.tile(np.array(dps),(361,720,1))
UDP = np.multiply(uwnd,dps)
moment = np.mean(UDP, axis=(1,2))
aam = np.multiply(np.multiply(moment,np.cos(lats[:,0]*rad)),twopi*radius_E3/gravity)
#aam = np.multiply(aam,twopi*radius_E3/gravity)
plt.plot(lats[:,0],aam)
plt.show()
print np.sum(aam)

		


