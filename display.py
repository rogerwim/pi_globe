import serial
import control
import os
import predict
import tkinter as tk
import sys
import getopt
import datetime
version = "v1.0"
laser_status = False
# can have dual tags, keep that in mind, might break stuff later
args,_ = getopt.getopt(sys.argv[1:], "dhvu", ["debug","help","version","unsafe"])
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
        print("-u,--unsafe diffent motor mode with start stop buttons, no deadmans switch")
        print("things like -dh are supported")
        exit()
    if parsed == "-v" or parsed == "--version":
        print("version:", version)
        exit()
    if parsed == "-u" or parsed == "--unsafe":
        motor_mode = True # false = press = execute release = stop, true = seprate buttons
    else:
        motor_mode = False # false = press = execute release = stop, true = seprate buttons
root = tk.Tk()
root.title("globe GUI")
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)
frame2 = tk.Frame(root)
frame2.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)
lat = tk.StringVar()
long = tk.StringVar()
def q():
    window.destroy()
def p():
    sate = e1.get()
    predict.setup_list()
    predict.filter_list(sate)
    listbox.delete(0,tk.END)
    for element in predict.output:
        listbox.insert(tk.END, element[0])
tracking = False
def t():
    global tracking
    tracking = True
def r():
    global tracking
    tracking = False
def g():
    global laser_status
    laser_status = not laser_status
    control.set_laser(int(laser_status))
def e():
    steps = int(e2.get())
    control.step_without_home(steps)
def servo():
    steps = int(e3.get())
    control.servo_goto(steps)
listbox = tk.Listbox(frame2)
listbox.pack(side = tk.LEFT, fill = tk.BOTH)
scrollbar = tk.Scrollbar(frame2)
scrollbar.pack(side = tk.LEFT, fill=tk.Y)
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
tk.Button(frame, text='stop tracking', command=r).grid(row=3, column=4, sticky=tk.W, pady=4) 
if debug:
    window = tk.Toplevel(root)
    tk.Label(window,text="motor 1(stepper):").grid(row=3,column=0)
    tk.Label(window,text="servo:").grid(row=6,column=0)
    tk.Label(window,text="laser:").grid(row=1,column=0)
    tk.Button(window, text='toggle', command=g).grid(row=2, column=0)
    tk.Button(window, text='exit window', command=q).grid(row=0, column=0)
    window.title("debug window")
    global e2
    e2 = tk.Entry(window)
    e2.grid(row=4,column=1)
    tk.Label(window,text="angle to turn:").grid(row=4,column=0)
    tk.Button(window, text='execute', command=e).grid(row=5, column=0)
    global e3
    e3 = tk.Entry(window)
    e3.grid(row=7,column=1)
    tk.Label(window,text="angle to turn:").grid(row=7,column=0)
    tk.Button(window, text='execute', command=servo).grid(row=8, column=0)
import time
while 1:
    root.update_idletasks()
    root.update()
    time.sleep(1/15)
    owe = 0
    if tracking:
        prev_loc = [0,0]
        control.home()
        for i in range(10):
            date = datetime.datetime(1,1,1).now()
            index = listbox.curselection()
            if index:
                index = index[0]
                satelite = predict.output[index]
            else:
                satelite = ['ISS (ZARYA)', 80]
            print(satelite)
            loc = predict.track(satelite[1],date)
            delta_long = loc[1] - prev_loc[1]
            owe += delta_long
            print("latitude:",loc[0],"longitude:",loc[1])
            lat.set("{:.4f}".format(loc[0]))
            long.set("{:.4f}".format(loc[1]))
            if owe > 2:
                control.step_without_home(-owe)
                owe -= owe
            print(f"OWE {owe} STEPS")
            control.servo_goto(int(loc[0]))
            time.sleep(10)
            prev_loc = loc
            root.update_idletasks()
            root.update()
            if not tracking:
                break
        control.home()
