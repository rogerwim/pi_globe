import os
import predict
import tkinter as tk
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
listbox = tk.Listbox(root)
listbox.pack(side = tk.LEFT, fill = tk.BOTH)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
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
tk.mainloop()
