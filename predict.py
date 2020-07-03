import ephem
import satelite
import time
f = open("tle.txt","r")
a = f.readlines()
f.close()
line1s = []
line2s = []
line3s = []
temp = 0
for i in range(0,len(a)-1,3):
	line1s.append(a[i+0].strip())
	line2s.append(a[i+1].strip())
	line3s.append(a[i+2].strip())
print("found:",len(line1s),"satelites using tle.txt")
c = []
for i in range(len(line1s)):
	c.append([line1s[i],i])
c.sort()
def check(x,filt):
	if filt in x[0]:
		return True
	return False
def Main():
	filt = input("enter name filter:")
	filt = filt.upper()
	matches = []
	for i in c:
		if check(i,filt):
			matches.append(i)
	for e in matches:
		print(e)
	sate = input("enter satelite number to track: ")
	for a in c:
		if a[1] == int(sate):
			print("this is", a[0])
			temp = a[1]
	line1 = line1s[temp]
	line2 = line2s[temp]
	line3 = line3s[temp]
	print(line1,"\n",line2,"\n",line3)
	s = satelite.load(line1,line2,line3)
	for i in range(20):
		pos = satelite.get_sat_pos(ephem.Moon())
		print(pos[0],pos[1])
		time.sleep(1)
	Main()
Main()
