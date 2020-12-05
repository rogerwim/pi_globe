import serial
import os
import predict
import tkinter as tk
import sys
import getopt
import laser
s = serial.Serial("/dev/ttyACM0",115200, timeout=1)
laser.setup(s)
version = "v1.0"
laser_status = False
# can have dual tags, keep that in mind, might break stuff later
args,_ = getopt.getopt(sys.argv[1:], "dhv", ["debug","help","version"])
debug = False
for argument in args:
	parsed = argument[:1][0]
	if parsed == "-d" or parsed == "--debug":
		debug = True
		print("debug mode on")
	if parsed == "-h" or parsed == "--help":
		print("HELP:")
		print("-h,--help print this help and exit")
		print("-v,--version print version and exit")
		print("-d,--debug enable debug mode")
		print("things like -dh are supported")
		exit()
	if parsed == "-v" or parsed == "--version":
		print("version:", version)
		exit()
root = tk.Tk()
root.title("globe GUI")
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)
lat = tk.StringVar()
long = tk.StringVar()
def p():
	sate = e1.get()
	predict.setup_list()
	predict.filter_list(sate)
	listbox.delete(0,tk.END)
	for element in predict.output:
		listbox.insert(tk.END, element[0])
def t():
	index = listbox.curselection()[0]
	satelite = predict.output[index]
	print(satelite)
	loc = predict.track(satelite[1])
	print("latitude:",loc[0],"longitude:",loc[1])
	lat.set("{:.4f}".format(loc[0]))
	long.set("{:.4f}".format(loc[1]))
def g():
	global laser_status
	laser_status = not laser_status
	if laser_status:
		laser.on()
	if not laser_status:
		laser.off()
	print(laser_status)
listbox = tk.Listbox(root)
listbox.pack(side = tk.LEFT, fill = tk.BOTH)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side = tk.LEFT, fill = tk.BOTH)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)
tk.Label(frame,text="Search for:").grid(row=0, column=0)
tk.Label(frame,text="latitude: ").grid(row=1, column=0)
tk.Label(frame,textvariable=lat).grid(row=1, column=1)
tk.Label(frame,text="   longitude: ").grid(row=2, column=0)
tk.Label(frame,textvariable=long).grid(row=2, column=1)
e1 = tk.Entry(frame)
e1.grid(row=0, column=1)
tk.Button(frame, text='Quit', command=root.destroy).grid(row=3, column=0, sticky=tk.W, pady=4) #root.destroy
tk.Button(frame, text='Show', command=p).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.Button(frame, text='track selected', command=t).grid(row=3, column=2, sticky=tk.W, pady=4) 
tk.Button(frame, text='laser toggle', command=g).grid(row=3, column=3, sticky=tk.W, pady=4)
tk.mainloop()
