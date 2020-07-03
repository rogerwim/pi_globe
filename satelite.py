from sgp4.api import Satrec
from sgp4.api import days2mdhms
import ephem
import re
import time
yr = []
def load(line1=" ",line2=" ",line3=" "):
	if line1 == " " and line2 == " " and line3 == " ":
		line1 = "ISS (ZARYA)"
		line2 = "1 25544U 98067A   20164.65373352  .00000382  00000-0  14906-4 0  9994"
		line3 = "2 25544  51.6454  10.9046 0002538  44.6307  63.7290 15.49438511231317"
	satellite = Satrec.twoline2rv(line2, line3)
	yr = satellite.epochyr
	a = days2mdhms(satellite.epochyr, satellite.epochdays)
	print("year:",yr,"month:",a[0],"day:",a[1],"hour:",a[2])
	print("if this is > 2 weeks ago replace the tle's")
	sat = ephem.readtle(line1, line2, line3)
	return sat
def c(d, m, s):
	if float(d) < 0:
		dd = float(d) - float(m)/60 - float(s)/3600
		return dd
	else:
		dd = float(d) + float(m)/60 + float(s)/3600
		return dd
def get_sat_pos(sat):
	sat.compute()
	a = str(sat.sublong)
	b = str(sat.sublat)
	a = a.split(":")
	b = b.split(":")
	a = c(a[0],a[1],a[2])
	b = c(b[0],b[1],b[2])
	return [a,b]
