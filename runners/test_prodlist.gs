function gradsrunner(args)
 modname=subwrd(args,1)
 fhour=subwrd(args,2)
 sector=subwrd(args,3)
*'run /home/scripts/grads/prodscripts/radarrefc.gs 'modinit' 'modname' 'fhour' 'sector
*'run /home/scripts/grads/prodscripts/stp.gs 'modinit' 'modname' 'fhour' 'sector
*'run /home/scripts/grads/prodscripts/hrrrsbcape.gs 'modinit' 'modname' 'fhour' 'sector
*'run /home/scripts/grads/prodscripts/uphlcy.gs 'modinit' 'modname' 'fhour' 'sector
'run /home/vgensini/aam/prodscripts/500wind.gs 'modname' 'fhour' 'sector
*'run /home/scripts/grads/prodscripts/svg.gs 'modinit' 'modname' 'fhour' 'sector
*'run /home/scripts/grads/prodscripts/2mdewpt.gs 'modinit' 'modname' 'fhour' 'sector
*'run /home/scripts/grads/prodscripts/hrrrptype.gs 'modinit' 'modname' 'fhour' 'sector
*'run /home/scripts/grads/prodscripts/windgust.gs 'modinit' 'modname' 'fhour' 'sector
*'run /home/scripts/grads/prodscripts/kuchsnowaccum.gs 'modinit' 'modname' 'fhour' 'sector
*'run /home/scripts/grads/prodscripts/visibility.gs 'modinit' 'modname' 'fhour' 'sector
*if fhour != 000
* 'run /home/scripts/grads/prodscripts/uphlcy_swath.gs 'modinit' 'modname' 'fhour' 'sector
* 'run /home/scripts/grads/prodscripts/snowaccum.gs 'modinit' 'modname' 'fhour' 'sector
* 'run /home/scripts/grads/prodscripts/precaccum.gs 'modinit' 'modname' 'fhour' 'sector
* 'run /home/scripts/grads/prodscripts/zraccum.gs 'modinit' 'modname' 'fhour' 'sector
*endif
