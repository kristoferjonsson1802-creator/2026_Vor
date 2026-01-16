import sys
from tkinter import *

def einn():
    textDisplay.insert(END,1)
    return
def tveir():
    textDisplay.insert(END,2)
    return
def þrir():
    textDisplay.insert(END,3)
    return
def fjorir():
    textDisplay.insert(END,4)
    return
def fimm():
    textDisplay.insert(END,5)
    return
def sex():
    textDisplay.insert(END,6)
    return
def sjo():
    textDisplay.insert(END,7)
    return
def atta():
    textDisplay.insert(END,8)
    return
def niu():
    textDisplay.insert(END,9)
    return
def null():
    textDisplay.insert(END,0)
    return
def slash():
    textDisplay.insert(END,'/')
    return
def stjarna():
    textDisplay.insert(END,'*')
    return
def minus():
    textDisplay.insert(END,'-')
    return
def eyda():
    textDisplay.delete(0, END)
    return
def samasem():
    textDisplay.insert(END,'=')
    return
def plus():
    textDisplay.insert(END,'+')
    return

#gluggi
root=Tk()
root.title('Calc is short for calculator btw')

#gera breytur 
num1 = StringVar()

#frames
frame0 = Frame(root)
frame0.pack(side=TOP)
textDisplay=Entry(frame0, textvariable=num1, bd=20, insertwidth=1, font=30)
textDisplay.pack(side = TOP)
frame1 = Frame(root)
frame1.pack(side=TOP)
frame2 = Frame(root)
frame2.pack(side=TOP)
frame3 = Frame(root)
frame3.pack(side=TOP)
frame4 = Frame(root)
frame4.pack(side=TOP)


#buttons
button1=Button(frame1, padx=16, bd=8, fg='Black', text='1', command=einn)
button1.pack(side=LEFT)
button1.config(height=1, width=2)
button2=Button(frame1, padx=16, bd=8, fg='Black', text='2', command=tveir)
button2.pack(side=LEFT)
button2.config(height=1, width=2)
button3=Button(frame1, padx=16, bd=8, fg='Black', text='3', command=þrir)
button3.pack(side=LEFT)
button3.config(height=1, width=2)
button4=Button(frame1, padx=16, bd=8, fg='Black', text='/', command=slash)
button4.pack(side=LEFT)
button4.config(height=1, width=2)

button5=Button(frame2, padx=16, bd=8, fg='Black', text='4', command=fjorir)
button5.pack(side=LEFT)
button5.config(height=1, width=2)
button6=Button(frame2, padx=16, bd=8, fg='Black', text='5', command=fimm)
button6.pack(side=LEFT)
button6.config(height=1, width=2)
button7=Button(frame2, padx=16, bd=8, fg='Black', text='6', command=sex)
button7.pack(side=LEFT)
button7.config(height=1, width=2)
button8=Button(frame2, padx=16, bd=8, fg='Black', text='*', command=stjarna)
button8.pack(side=LEFT)
button8.config(height=1, width=2)

button9=Button(frame3, padx=16, bd=8, fg='Black', text='7', command=sjo)
button9.pack(side=LEFT)
button9.config(height=1, width=2)
button10=Button(frame3, padx=16, bd=8, fg='Black', text='8', command=atta)
button10.pack(side=LEFT)
button10.config(height=1, width=2)
button11=Button(frame3, padx=16, bd=8, fg='Black', text='9', command=niu)
button11.pack(side=LEFT)
button11.config(height=1, width=2)
button12=Button(frame3, padx=16, bd=8, fg='Black', text='-', command=minus)
button12.pack(side=LEFT)
button12.config(height=1, width=2)

button13=Button(frame4, padx=16, bd=8, fg='Black', text='C', command=eyda)
button13.pack(side=LEFT)
button13.config(height=1, width=2)
button14=Button(frame4, padx=16, bd=8, fg='Black', text='0', command=null)
button14.pack(side=LEFT)
button14.config(height=1, width=2)
button15=Button(frame4, padx=16, bd=8, fg='Black', text='=', command=samasem)
button15.pack(side=LEFT)
button15.config(height=1, width=2)
button16=Button(frame4, padx=16, bd=8, fg='Black', text='+', command=minus)
button16.pack(side=LEFT)
button16.config(height=1, width=2)

root.mainloop()
