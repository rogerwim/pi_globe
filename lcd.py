# TODO pass laser through to pins.py
import shift_reg
def set(rs,d7,d6,d5,d4):
	shift_reg.shift([0,0,0,0,0,0])
	shift_reg.shift([d4,d5,d6,d7,rs,0])
	shift_reg.shift([d4,d5,d6,d7,rs,1])
	shift_reg.shift([d4,d5,d6,d7,rs,0])
	shift_reg.shift([0,0,0,0,0,0])
def init():
	set(0,0,0,1,0)

	set(0,0,0,1,0)
	set(0,1,0,0,0)

	set(0,0,0,0,0)
	set(0,1,1,1,0)

	set(0,0,0,0,0)
	set(0,0,1,1,0)

	set(0,0,0,0,0)
	set(0,0,0,0,1)

def write(letter):
	data = ord(letter)
	data1 = data >> 4 & 15
	data2 = data & 15
	set(1,(data1 >> 3) & 1,(data1 >> 2) & 1,(data1 >> 1) & 1,(data1 >> 0) & 1)
	set(1,(data2 >> 3) & 1,(data2 >> 2) & 1,(data2 >> 1) & 1,(data2 >> 0) & 1)
def put(text):
	for letter in text:
		write(letter)
def clear():
	set(0,0,0,0,0)
	set(0,0,0,0,1)
def move(left,right):
	if (left and right) or not (left or right):
		raise ValueError("NONSENSE")
	if left:
		set(0,0,0,0,1)
		set(0,0,0,0,0)
	if right:
		set(0,0,0,0,1)
		set(0,0,1,0,0)
