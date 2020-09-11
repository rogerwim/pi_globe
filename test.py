import serial
s = serial.Serial("/dev/ttyACM0",115200, timeout=1)
def write(pin2,pin3,pin4,motor1_forward,motor1_reverse,motor2_forward,motor2_reverse,motor_stop):
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
	print(z)
	print(bytes([z]))
	s.write(bytes([z]))
	s.write(bytes([y]))
	s.flush()
