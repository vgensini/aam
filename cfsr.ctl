dset /home/vgensini/data/CFSR/cfsr_198001.grb2
index /home/vgensini/data/CFSR/cfsr_198001.grb2.idx
undef 9.999E+20
title /home/vgensini/data/CFSR/cfsr_198001.grb2
* produced by g2ctl v0.0.9
* command line options: /home/vgensini/data/CFSR/cfsr_198001.grb2
* griddef=5:504349:(720 x 361):grid_template=0:winds(N/S): lat-lon grid:(720 x 361) units 1e-06 input WE:NS output WE:SN res 48 lat 90.000000 to -90.000000 by 0.500000 lon 0.000000 to 359.500000 by 0.500000 #points=259920:winds(N/S)

dtype grib2
ydef 361 linear -90.000000 0.5
xdef 720 linear 0.000000 0.500000
tdef 124 linear 00Z01jan1980 6hr
* PROFILE hPa
zdef 37 levels 100000 97500 95000 92500 90000 87500 85000 82500 80000 77500 75000 70000 65000 60000 55000 50000 45000 40000 35000 30000 25000 22500 20000 17500 15000 12500 10000 7000 5000 3000 2000 1000 700 500 300 200 100
options pascals
vars 5
HGTsfc   0,1,0   0,3,5 ** surface Geopotential Height [gpm]
HGTprs    37,100  0,3,5 ** (1000 975 950 925 900.. 7 5 3 2 1) Geopotential Height [gpm]
PRMSLmsl   0,101,0   0,3,1 ** mean sea level Pressure Reduced to MSL [Pa]
UGRDprs    37,100  0,2,2 ** (1000 975 950 925 900.. 7 5 3 2 1) U-Component of Wind [m/s]
VGRDprs    37,100  0,2,3 ** (1000 975 950 925 900.. 7 5 3 2 1) V-Component of Wind [m/s]
ENDVARS
