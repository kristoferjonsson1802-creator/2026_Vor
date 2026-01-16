from tkinter import *
import tkinter.messagebox

gluggi = Tk() 
gluggi.title('Verkefni 1') 
gluggi.geometry('450x300') 

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

labelText = StringVar()
labelText.set('Spilari1       <<<<<<<       Spilari2')
labell = Label(frame0, textvariable=labelText, height=4) 
labell.pack() 

labelText = StringVar()
labelText.set('Byrjaðu að spila       Byrjaðu að spila')
labell = Label(frame1, textvariable=labelText, height=4) 
labell.pack() 

custName = StringVar(None) 
yourName = Entry(frame2, textvariable=custName) 
yourName.pack(side = LEFT, padx=15) 
custName = StringVar(None) 
yourName = Entry(frame2, textvariable=custName) 
yourName.pack(side = LEFT, padx=15) 

button1=Button(frame3, padx=20, pady=7, bd=8, fg='Black', text='Draga spil')
button1.pack(side=LEFT, padx = 5)
button1.config(height=1, width=2)
button2=Button(frame3, padx=20, pady=7, bd=8, fg='Black', text='Hætta')
button2.pack(side=LEFT, padx = 5)
button2.config(height=1, width=2)

button3=Button(frame3, padx=20, pady=7, bd=8, fg='Black', text='Draga spil')
button3.pack(side=LEFT, padx = 5)
button3.config(height=1, width=2)
button4=Button(frame3, padx=20, pady=7, bd=8, fg='Black', text='Hætta')
button4.pack(side=LEFT, padx = 5)
button4.config(height=1, width=2)

button5=Button(frame4, padx=40, pady=7, bd=8, fg='Black', text='Byrja upp á nýtt')
button5.pack(side=LEFT)
button5.config(height=1, width=2)
