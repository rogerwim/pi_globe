import pins
def setup(serial):
	pins.setup(serial)
def on():
	pins.write(laser_on=1)
def off():
	pins.write(laser_off=1)
