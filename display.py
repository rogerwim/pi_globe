import serial
import control
import os
import predict
import tkinter as tk
import sys
import getopt
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
    pass
def e():
    pass
def forward(event=None):
    pass
def backward(event=None):
    pass
def stop(event=None):
    pass
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
    tk.Label(window,text="motor 2(DC):").grid(row=6,column=0)
    tk.Label(window,text="laser:").grid(row=1,column=0)
    tk.Button(window, text='toggle', command=g).grid(row=2, column=0)
    tk.Button(window, text='exit window', command=q).grid(row=0, column=0)
    window.title("debug window")
    global e2
    e2 = tk.Entry(window)
    e2.grid(row=4,column=1)
    tk.Label(window,text="angle to turn:").grid(row=4,column=0)
    tk.Button(window, text='execute', command=e).grid(row=5, column=0)
    a = tk.Button(window, text='forward')
    a.grid(row=7, column=0)
    b = tk.Button(window, text='backward')
    b.grid(row=7, column=1)
    if not motor_mode:
        a.bind('<ButtonPress-1>',forward)
        a.bind('<ButtonRelease-1>',stop)
        b.bind('<ButtonPress-1>',backward)
        b.bind('<ButtonRelease-1>',stop)
    else:
        c = tk.Button(window, text='stop')
        c.grid(row=7, column=2)
        a.bind('<ButtonPress-1>',forward)
        b.bind('<ButtonPress-1>',backward)
        c.bind('<ButtonPress-1>',stop)
import time
while 1:
    root.update_idletasks()
    root.update()
    time.sleep(1/15)
    if tracking:
        prev_loc = [0,0]
        for i in range(5):
            index = listbox.curselection()[0]
            satelite = predict.output[index]
            print(satelite)
            loc = predict.track(satelite[1])
            delta_long = loc[1] - prev_loc[1]
            print("latitude:",loc[0],"longitude:",loc[1])
            lat.set("{:.4f}".format(loc[0]))
            long.set("{:.4f}".format(loc[1]))
            control.step_without_home(delta_long)
            control.servo_goto(int(loc[0]))
            time.sleep(10)
            prev_loc = loc
        control.home()
