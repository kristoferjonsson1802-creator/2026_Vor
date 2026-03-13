from tkinter import *
import tkinter.messagebox

def beenClicked():
    radioValue = relStatus.get()
    tkinter.messagebox.showinfo('þú ýttir á', radioValue)

def pontun():
    name = yourName.get()
    size = relStatus.get()
    ptype = relStatus1.get()
    tkinter.messagebox.showinfo('Pöntunin', name + ' pantaði ' + size + ' ' + ptype)

gluggi = Tk() 
gluggi.title('PizzaPöntun')
gluggi.geometry('450x400')

frame0 = Frame(gluggi)
frame0.pack(side=TOP)
frame1 = Frame(gluggi)
frame1.pack(side=TOP)
frame2 = Frame(gluggi)
frame2.pack(side=TOP)
frame3 = Frame(gluggi)
frame3.pack(side=TOP)
frame4 = Frame(gluggi)
frame4.pack(side=TOP)
frame5 = Frame(gluggi)
frame5.pack(side=TOP)

labelText = StringVar()
labelText.set('----------PizzaPöntun----------')
labell = Label(frame0, textvariable=labelText, height=4) 
labell.pack()

labelText = StringVar()
labelText.set('Nafn:')
labell = Label(frame1, textvariable=labelText, height=4) 
labell.pack(side=LEFT)

custName = StringVar()
yourName = Entry(frame1, textvariable=custName) 
yourName.pack(side=LEFT)

labelText = StringVar()
labelText.set('Stærð:')
labell = Label(frame2, textvariable=labelText, height=4) 
labell.pack(side=LEFT)

relStatus = StringVar()
relStatus.set(None)
Radiobutton(frame2, text='Lítil', value='Litla', variable=relStatus, command=beenClicked).pack(side=LEFT)
Radiobutton(frame2, text='Mið', value='Miðstærð', variable=relStatus, command=beenClicked).pack(side=LEFT)
Radiobutton(frame2, text='Stór', value='Stóra', variable=relStatus, command=beenClicked).pack(side=LEFT)

labelText = StringVar()
labelText.set('Hvernig Pizzu:')
labell = Label(frame3, textvariable=labelText, height=4) 
labell.pack(side=LEFT)

relStatus1 = StringVar()
relStatus1.set(None)
Radiobutton(frame3, text='Kjöt', value='Kjöt Pizzu', variable=relStatus1).pack(side=LEFT)
Radiobutton(frame3, text='Osta', value='Osta Pizzu', variable=relStatus1).pack(side=LEFT)
Radiobutton(frame3, text='Vegan', value='Vegan Pizzu', variable=relStatus1).pack(side=LEFT)

labelText = StringVar()
labelText.set('Auka áleg:')
labell = Label(frame4, textvariable=labelText, height=4) 
labell.pack(side=LEFT)

checkBoxVal1 = StringVar()
Checkbutton(frame4, variable=checkBoxVal1, text='Extra Pepperoni').pack(side=LEFT)
checkBoxVal2 = StringVar()
Checkbutton(frame4, variable=checkBoxVal2, text='Extra ost').pack(side=LEFT)
checkBoxVal3 = StringVar()
Checkbutton(frame4, variable=checkBoxVal3, text='Hvítlaukssósu').pack(side=LEFT)

button1 = Button(frame5, padx=20, pady=7, bd=8, fg='Black', text='Panta Pizzu', command=pontun)
button1.pack(padx=5)
button1.config(height=1, width=10)

gluggi.mainloop()
