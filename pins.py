import serial
def setup(serial):
	global s
	s = serial
laser = 0
def write(pin2=0,pin3=0,pin4=0,motor1_forward=0,motor1_reverse=0,motor2_forward=0,motor2_reverse=0,motor_stop=0,laser_on=0,laser_off=0):
	global laser
	if laser_on == 1:
		laser = 1
	if laser_off == 1:
		laser = 0
	if laser_on and laser_off:
		raise ValueError("no thanks, WHAT DO YOU WANT")
	z = 0
	y = 0
	z += pin2 << 0
	z += pin3 << 1
	z += pin4 << 2
	z += motor1_forward << 3
	z += motor1_reverse << 4
	z += motor2_forward << 5
	z += motor2_reverse << 6
	y += motor_stop << 0
	y += laser << 1
	s.write(bytes([z]))
	s.write(bytes([y]))
	s.flush()
	print(bytes([z]))
	print(bytes([y]))
def get():
	global laser
	return laser
def set(la):
	global laser
	laser = la
