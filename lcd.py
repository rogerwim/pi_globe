import serial
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = serial.Serial("/dev/ttyAMA0")
sock.bind(("0.0.0.0",30))
sock.listen(1)
a_old = ""
while True:
 conn,addr = sock.accept()
 print(addr[0], "has entered the chat")
 while True:
  a = conn.recv(1000)
  print(a.decode())
  s.write(a)
  if a.decode() == "":
   print(addr[0], "has left the chat")
   break
  if a.decode().strip("") == "get":
   conn.sendall(a_old)
  a_old = a
