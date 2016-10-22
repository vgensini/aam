*Purpose: College of DuPage Models Product Shell
*Author: Gensini, Winter 2015
*************************************************************************
*always run this function to get model arguments and plotting defaults
function main(args)
 modname=subwrd(args,1)
 fhour=subwrd(args,2)
 sector=subwrd(args,3)
 'run /home/vgensini/aam/functions/pltdefaults.gs'
*GLOBAL VARIABLES
filext = '.png'
txtext = '.txt'
basedir = '/home/vgensini/aam'
*************************************************************************
*open the GrADS .ctl file made in the prodrunner script
'open /home/vgensini/aam/cfsr.ctl'
'set t 'fhour/6+1
*get some time parameters
*'run /home/scripts/grads/functions/timelabel.gs 'modinit' 'modname' 'fhour
*set domain based on sector input argument
'run /home/vgensini/aam/functions/sectors.gs 'sector
*START: PRODUCT SPECIFIC ACTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*give the image a product title
'draw string 0.1 8.3 500mb Isotachs (kts) | Geopotential Height (gpm) | Victor Gensini'
*give the product a name between sector and fhour variables and combo into filename variables
prodname = modname sector _500_spd_ fhour
filename = basedir'/'prodname%filext
*pick a colorbar
'run /home/vgensini/aam/colorbars/color.gs 0 150 5 -kind white->(200,200,200)->steelblue->thistle->purple->crimson->khaki->darkgoldenrod'
*set level (set both!)
level = 500
'set lev 'level
'run /home/vgensini/aam/functions/isotachs.gs 'modname' 'level
'run /home/vgensini/aam/functions/interstates.gs 'sector
'run /home/vgensini/aam/functions/states.gs 'sector
'set cint 60'
'run /home/vgensini/aam/functions/isoheights.gs 'modname' 'level
if sector != WLD
 'run /home/vgensini/aam/functions/windbarb.gs 'sector' 'modname' 'level
endif
*plot the colorbar on the image
'run /home/vgensini/aam/functions/pltcolorbar.gs -ft 1 -fy 0.33 -line on -fskip 4 -fh .1 -fw .1 -lc 99 -edge triangle -fc 99'
*generate the image
'run /home/vgensini/aam/functions/make_image.gs 'filename
