import os
from sgp4.api import Satrec
from sgp4.api import days2mdhms
import ephem
import re
import time
import datetime
yr = []
def load(line1=None,line2=None,line3=None):
	if line1 == None or line2 == None or line3 == None:
		print("A LINE IS EMPTY ASSUMING ISS, THIS ISN'T NORMAL")
		line1 = "ISS (ZARYA)"
		line2 = "1 25544U 98067A   20164.65373352  .00000382  00000-0  14906-4 0  9994"
		line3 = "2 25544  51.6454  10.9046 0002538  44.6307  63.7290 15.49438511231317"
	satellite = Satrec.twoline2rv(line2, line3)
	yr = satellite.epochyr
	a = days2mdhms(satellite.epochyr, satellite.epochdays)
	yr = int("20" + str(yr))
	now = datetime.datetime.now()
	last_r = datetime.datetime(yr,a[0],a[1],a[2])
	delta = datetime.timedelta(days=14)
	max_datetime = delta + last_r
	print(now,last_r,max_datetime)
	if now > max_datetime:
		print("running ./tle.sh")
		error_code = os.system("./tle.sh")
		if error_code:
			print("something went wrong, check internet")
			exit()
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
	a = str(sat.sublat)
	b = str(sat.sublong)
	a = a.split(":")
	b = b.split(":")
	a = c(a[0],a[1],a[2])
	b = c(b[0],b[1],b[2])
	return [a,b]
