import serial
arduino = serial.Serial
def goto(pos):
    print(pos)
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
    return byte
def send_command(command, data1,data2,data3,data4,data5,data6): # example command [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    command1 = 0
    command2 = 0
    print(command)
    command1 = bits_to_byte(command[0:8])
    command2 = bits_to_byte(command[8:])
    print(command1,command2)
