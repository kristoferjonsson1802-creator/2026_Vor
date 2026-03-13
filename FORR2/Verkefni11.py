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

def conversion2():
    if celsius_entry.get() and not fahrenheit_entry.get():
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_entry.delete(0, END)
        fahrenheit_entry.insert(0, round(fahrenheit, 2))

    elif fahrenheit_entry.get() and not celsius_entry.get():
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_entry.delete(0, END)
        celsius_entry.insert(0, round(celsius, 2))

gluggi = Tk() 
gluggi.title('conversion2') 
gluggi.geometry('250x150') 

frame0 = Frame(gluggi)
frame0.pack(side = TOP)
frame1 = Frame(gluggi)
frame1.pack(side = TOP)
frame2 = Frame(gluggi)
frame2.pack(side = TOP)
frame3 = Frame(gluggi)
frame3.pack(side = TOP)
frame4 = Frame(gluggi)
frame4.pack(side = TOP)
frame5 = Frame(gluggi)
frame5.pack(side = TOP)

Label(frame0, text="Meter:").grid(row=0, column=0, sticky='e')
meter_entry = Entry(frame0)
meter_entry.grid(row=0, column=1, padx=2, pady=2)

Label(frame1, text="Feet:").grid(row=0, column=0, sticky='e')
feet_entry = Entry(frame1)
feet_entry.grid(row=0, column=1, padx=2, pady=2)

Label(frame3, text="Celsius:").grid(row=0, column=0, sticky='e')
celsius_entry = Entry(frame3)
celsius_entry.grid(row=0, column=1, padx=2, pady=2)

Label(frame4, text="Fahrenheit:").grid(row=0, column=0, sticky='e')
fahrenheit_entry = Entry(frame4)
fahrenheit_entry.grid(row=0, column=1, padx=2, pady=2)

Button(frame2, text="Reikna", command=conversion).pack()
Button(frame5, text="Reikna", command=conversion2).pack()

gluggi.mainloop()
