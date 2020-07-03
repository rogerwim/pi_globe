from time import sleep
import test
def out(data):
	test.write(data,0,0,0,0,0,0)
def start():
	sleep(2)
	out(0)
	sleep(0.5)
	out(1)
	sleep(0.5)
def send_byte(b):
	out(0)
	for i in range(-7,1):
		out((b >> -i) & 1)
		sleep(0.05)
	out(1)
	sleep(0.2)
def Main():
	start()
	m = input("message: ")
	m = m.encode()
	for b in m:
		send_byte(int(b))
Main()
