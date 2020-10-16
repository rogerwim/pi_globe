import pins as test
import time
def set(strobe,data,clock):
	test.write(strobe,data,clock,0,0,0,0,0)
def shift_out(bit):
	set(0,0,0)
	time.sleep(0.0001)
	set(0,bit,0)
	time.sleep(0.0001)
	set(0,bit,1)
	time.sleep(0.0001)
	set(0,0,0)
def shift(bits):
	time.sleep(0.0001)
	bits.reverse()
	for bit in bits:
		shift_out(bit)
	set(1,0,0)
	time.sleep(0.0001)
set(0,0,0)
time.sleep(0.0001)
