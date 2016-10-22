#!/usr/bin/csh
foreach FHour (000 006 012 018 024 030 036 042 048 054 060 066 072 078 084)
	foreach Sector (PO)
		grads -bxcl "run /home/vgensini/aam/runners/test_prodlist.gs CFSR ${FHour} ${Sector}" &
	end
end
wait
