import sys
from tkinter import *

def raudur():
    labell.config(bg='Red')
    return

def blar():
    labell.config(bg='Blue')
    return

def gulur():
    labell.config(bg='Yellow')
    return

def svartur():
    labell.config(bg='Black')
    return

def hvitur():
    labell.config(bg='White')
    return

root = Tk()
root.title('colors')
root.geometry('300x200')

frame0 = Frame(root)
frame0.pack(side = TOP)
frame1 = Frame(root)
frame1.pack(side = TOP)
frame2 = Frame(root)
frame2.pack(side = TOP)

button1=Button(frame0, padx=20, pady=20, bd=8, fg='Black', bg='Red', text='Rauður', command=raudur)
button1.pack(side=LEFT)
button1.config(height=1, width=2)
button2=Button(frame0, padx=20, pady=20, bd=8, fg='Black', bg='Blue', text='Blár', command=blar)
button2.pack(side=LEFT)
button2.config(height=1, width=2)
button3=Button(frame0, padx=20, pady=20, bd=8, fg='Black', bg='Yellow', text='Gulur', command=gulur)
button3.pack(side=LEFT)
button3.config(height=1, width=2)

button4=Button(frame1, padx=20, pady=20, bd=8, fg='White', bg='Black', text='Svartur', command=svartur)
button4.pack(side=LEFT)
button4.config(height=1, width=2)
button5=Button(frame1, padx=20, pady=20, bd=8, fg='Black', bg='White', text='Hvítur', command=hvitur)
button5.pack(side=LEFT)
button5.config(height=1, width=2)

LabelText = StringVar()
labell = Label(frame2, height=4, padx=150) 
labell.pack() 
