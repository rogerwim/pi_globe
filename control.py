import serial
steps_per_rev = 1440
arduino = serial.Serial('/dev/ttyUSB1',9600)
def bits_to_byte(bits):
    byte  = 0
    if type(bits) != list:
        raise TypeError("type must be list")
    if len(bits) != 8:
        raise ValueError("you must input 8 bits, no more or less")
    for i in range(0,8):
        if bits[i] != 1 and bits[i] != 0:
            raise TypeError("bits can only be 0 or 1")
        byte += bits[i] << i
    return bytes([byte])
def send_command(command, data1,data2,data3,data4,data5,data6): # example command [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    command1 = 0
    command2 = 0
    print(command)
    command1 = bits_to_byte(command[0:8])
    command2 = bits_to_byte(command[8:])
    print(command1,command2)
    data_and_command = command1 + command2 + bytes([data1]) + bytes([data2]) + bytes([data3]) + bytes([data4]) + bytes([data5]) + bytes([data6])
    print(data_and_command)
    arduino.write(data_and_command)
    print(arduino.read())
def step_with_home(ang):
    steps = (ang/360)*steps_per_rev
    print(steps)
    steps = int(steps)
    print(steps)
    data1 = (steps & 65280) >> 8
    data2 = (steps & 255) >> 0
    print(data1,data2)
    send_command([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],data1,data2,0,0,0,0)
def step_without_home(ang):
    steps = 1+((ang/360)*steps_per_rev)
    print(steps)
    steps = int(steps)
    print(steps)
    data1 = (steps & 65280) >> 8
    data2 = (steps & 255) >> 0
    print(data1,data2)
    send_command([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],data1,data2,0,0,0,0)
def home():
    send_command([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],0,0,0,0,0,0)
def servo_goto(ang):
    ang = ang + 90
    send_command([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],0,ang,0,0,0,0)
def set_laser(state):
    send_command([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],0,state,0,0,0,0)
