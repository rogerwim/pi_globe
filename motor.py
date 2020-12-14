import pins as test
import time
import math
angle = 0
steps_t = 0
s_per_t_1 = 200
def setup(ser):
	test.setup(ser)
def turn(ang):
	global angle
	global steps_t
	steps = math.floor((s_per_t_1/360)*ang)
	angle += ang
	steps_t = steps_t + steps
	diff = (s_per_t_1/360)*angle - steps_t
#difference between steps taken and steps we want to take = (steps per rotation/degrees in one turn)*total angle - total steps
	if steps < 0:
		steps = -steps
		for i in range(steps):
			test.write(0,0,0,0,1,0,0,0)
			time.sleep(0.05)
		steps = -steps
	if steps > 0:
		for i in range(steps):
			test.write(0,0,0,1,0,0,0,0)
			time.sleep(0.05)
	test.write(0,0,0,0,0,0,0,0)
def turn2(start,stop,reverse):
	if start:
        	test.write(0,0,0,0,0,1,0,0)
	if stop:
		test.write(0,0,0,0,0,0,0,1)
	if reverse:
		test.write(0,0,0,0,0,0,1,0)
def set(laser):
	test.set(laser)
def get():
	return test.get()
