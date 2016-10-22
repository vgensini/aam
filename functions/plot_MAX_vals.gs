'mfhilo prmslmsl/100 CL h 'radius', 'cint

High_info=result
i=2         ;*Since the data starts on the 2nd line
minmax=sublin(High_info,i)

while(subwrd(minmax,1) = 'H') 

  min_lat = subwrd(minmax, 2)
  min_lon = subwrd(minmax, 3)
  min_val = subwrd(minmax, 5)

  'q w2xy 'min_lon' 'min_lat      ;*Translate lat/lon to page coordinates
   x_min = subwrd(result,3)
   y_min = subwrd(result,6)


  'q gxinfo'                      ;*Get area boundaries
  xline=sublin(result,3)
  yline=sublin(result,4)
  xs=subwrd(xline,4)' 'subwrd(xline,6)
  ys=subwrd(yline,4)' 'subwrd(yline,6)

  if(y_min > subwrd(ys,1)+0.1 & y_min < subwrd(ys,2)-0.1 & x_min > subwrd(xs,1)+0.1 & x_min < subwrd(xs,2)-0.5)
    'set strsiz .28'
    'set string 4 c 9'
    'draw string 'x_min' 'y_min' H'
        
    'set strsiz 0.1'
    'set string 4 bl 2'
    'draw string 'x_min+0.1' 'y_min-0.15' 'min_val
  endif

  i=i+1
  minmax = sublin(High_info,i)
endwhile
