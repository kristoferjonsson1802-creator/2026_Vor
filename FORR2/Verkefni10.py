from tkinter import *

def conversion():
    if meter_entry.get() and not feet_entry.get():
        meters = float(meter_entry.get())
        feet = meters * 3.28084
        feet_entry.delete(0, END)
        feet_entry.insert(0, round(feet, 2))

    elif feet_entry.get() and not meter_entry.get():
        feet = float(feet_entry.get())
        meters = feet / 3.28084
        meter_entry.delete(0, END)
        meter_entry.insert(0, round(meters, 2))

gluggi = Tk() 
gluggi.title('conversion') 
gluggi.geometry('250x150') 

frame0 = Frame(gluggi)
frame0.pack(side = TOP)
frame1 = Frame(gluggi)
frame1.pack(side = TOP)
frame2 = Frame(gluggi)
frame2.pack(side = TOP)

Label(frame0, text="Meter:").grid(row=0, column=0, sticky='e')
meter_entry = Entry(frame0)
meter_entry.grid(row=0, column=1, padx=2, pady=2)

Label(frame1, text="Feet:").grid(row=0, column=0, sticky='e')
feet_entry = Entry(frame1)
feet_entry.grid(row=0, column=1, padx=2, pady=2)

Button(frame2, text="Reikna", command=conversion).pack()

gluggi.mainloop()