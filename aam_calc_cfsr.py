#!/usr/bin/python2.7
#########################################################################################################
#Purpose: Compute Global Relative Atmospheric Angular Momentum From CFS Reanalysis Data			#
#Inputs: 0.5 deg data obtained from CFS Reanalysis (CFSR)						#
#Assumptions: aam.so file exists in directory of this script						#			
#Misc Notes: aam.so was created using f2py from aam.f, originally used for AAM calculation 		#
#in NCL routines, slight modifications were necessary to the original aam.f code			#
#Outputs: Global Relative Atmospheric Angular Momentum kg*m^2/s (average value is 3 * 10^26 kg*m^2/s	#
#Created by: Victor Gensini (Fall 2016)									#
#########################################################################################################
import numpy as np
#import Nio as pynio
import sys,os,pygrib,aam,csv,datetime
start_input = '20060122' #YYYYMMDD
end_input  =  '20060122' #YYYYMMDD
begdate = datetime.datetime.strptime(start_input,"%Y%m%d") 
enddate = datetime.datetime.strptime(end_input,"%Y%m%d")
dates = []
while begdate <= enddate:
	dates.append(begdate)
	begdate+=datetime.timedelta(days=1)
AAM_vals=[]
file = open("AAM_climo.txt", "w")
for dt in dates:
	#filename = ("pgbhnl.gdas.%s%s%s-%s%s%s.grb2") % (dt.year,'%02d'%dt.month,'%02d'%dt.day,dt.year,'%02d'%dt.month,'%02d'%dt.day)
	#os.system("wget http://nomads.ncdc.noaa.gov/modeldata/cmd_pgbh/" + filename)
	filename = ("/home/vgensini/data/CFSR/cfsr_%s%s.grb2") % (dt.year, '%02d'%dt.month)
	gr = pygrib.open(filename)
	#for g in gr:
	#	print g.year, g.month, g.day, g.hour
	pres = gr.select(name ='Pressure reduced to MSL')[0]
	hghtmsgs = gr.select(name='Geopotential Height',typeOfLevel='isobaricInhPa', year=dt.year,month=dt.month,day=dt.day, hour=0)
	lats,lons = pres.latlons()
	pres = pres.values
	umsgs = gr.select(name='U component of wind',typeOfLevel='isobaricInhPa', year=dt.year,month=dt.month,day=dt.day, hour=0)
	plevs = []
	for h in hghtmsgs:
		plevs.append(h.level*100)
	plevs=np.array(plevs)
	x,y = pres.shape
	heights = np.zeros((len(plevs),x,y))
	uwnd = np.zeros((len(plevs),x,y))
	for i,(h,u) in enumerate(zip(hghtmsgs,umsgs)):
	  heights[i,:,:] = h.values
	  uwnd[i,:,:] = u.values			 
	#if modname == '1':
	#	dps=[1.,1.,2.,2.,3.,10.,10.,20.,20.,30.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,25.,25.,25.,25.,13.]
	#	AAM=aam.daamom1(uwnd,dps,np.arange(-90,91,1),np.ones(181),0.0)
	#elif modname == '.5':
	#	dps=[1.,1.,2.,2.,3.,10.,10.,20.,20.,30.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,25.,25.,25.,25.,13.]
	#	AAM=aam.daamom1(uwnd,dps,np.arange(-90,90.5,0.50),np.ones(361),0.0)
	#elif modname == '.25':
	#	dps=[1.,1.,2.,2.,3.,10.,10.,20.,20.,30.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,25.,25.,25.,25.,13.]
	#	AAM=aam.daamom1(uwnd,dps,np.arange(-90,90.25,0.25),np.ones(721),0.0)
	modname = 'CFS'
	if modname == 'CFS':
		dps=[0.,1.,2.,2.,3.,10.,10.,20.,20.,30.,25.,25.,25.,25.,25.,25.,50.,50.,50.,50.,50.,50.,50.,50.,50.,50.,25.,25.,25.,25.,25.,25.,25.,25.,25.,25.,0.]
		#dps=[100.,100.,200.,200.,300.,1000.,1000.,2000.,2000.,3000.,2500.,2500.,2500.,2500.,2500.,2500.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,5000.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,2500.,1300.]
		AAM=aam.daamom1(uwnd,dps,np.arange(-90,90.5,0.50),np.ones(361),0.0)
	#Sanity Check
	#if len(dps)==len(plevs):
		#print "All good! " + str(len(dps)) + ' Pressure Levels;' + str(len(plevs)) + ' Delta Pressure Levels'
	#else:
		#print "Uh oh. Mismatch. "  + str(len(dps)) + ' Pressure Levels;' + str(len(plevs)) + ' Delta Pressure Levels'
	#print '{:e}'.format(float(AAM))
	file.write(str(dt.year)+'-'+'{:02d}'.format(dt.month)+'-'+'{:02d}'.format(dt.day) + ','+str(float(AAM))+'\n')
file.close()

