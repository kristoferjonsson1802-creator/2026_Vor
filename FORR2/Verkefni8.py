from tkinter import *
import tkinter.messagebox

def beenClicked():
    radioValue = relStatus.get()
    tkinter.messagebox.showinfo('þú ýttir á', radioValue)
    return

def pontun():
    name = (yourName.get())
    Type = (relStatus.get())
    size = (relStatus.get1())
    tkinter.messagebox.showinfo('Pöntunin', name + ' Pantaði: ' + size, Type)
    return

gluggi = Tk() 
gluggi.title('PizzaPöntun')
gluggi.geometry('450x400')

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

labelText = StringVar()
labelText.set('----------PizzaPöntun----------')
labell = Label(frame0, textvariable=labelText, height=4) 
labell.pack()

labelText = StringVar()
labelText.set('Nafn:')
labell = Label(frame1, textvariable=labelText, height=4) 
labell.pack(side=LEFT)

custName = StringVar(None) 
yourName = Entry(frame1, textvariable=custName) 
yourName.pack(side=LEFT)

labelText = StringVar()
labelText.set('Stærð:')
labell = Label(frame2, textvariable=labelText, height=4) 
labell.pack(side=LEFT)

relStatus = StringVar()
relStatus.set(None)
radio1 = Radiobutton(frame2, text='Lítil', value='Litla', variable = relStatus, command = beenClicked).pack(side=LEFT)
radio1 = Radiobutton(frame2, text='Mið', value='Miðstærðs', variable = relStatus, command = beenClicked).pack(side=LEFT)
radio1 = Radiobutton(frame2, text='Stór', value='Stóra', variable = relStatus, command = beenClicked).pack(side=LEFT)

labelText = StringVar()
labelText.set('Hvernig Pizzu:')
labell = Label(frame3, textvariable=labelText, height=4) 
labell.pack(side=LEFT)

relStatus1 = StringVar()
relStatus.set(None)
radio2 = Radiobutton(frame3, text='Kjöt', value='Kjöt Pizzu', variable = relStatus1, command = beenClicked).pack(side=LEFT)
radio2 = Radiobutton(frame3, text='Osta', value='Osta Pizzu', variable = relStatus1, command = beenClicked).pack(side=LEFT)
radio2 = Radiobutton(frame3, text='Vegan', value='Vegan Pizzu', variable = relStatus1, command = beenClicked).pack(side=LEFT)

labelText = StringVar()
labelText.set('Auka áleg:')
labell = Label(frame4, textvariable=labelText, height=4) 
labell.pack(side=LEFT)

checkBoxVal = StringVar()
checkBox1 = Checkbutton(frame4, variable=checkBoxVal, text = 'Extra Pepperoni')
checkBox1.pack(side=LEFT)
checkBoxVal = StringVar()
checkBox2 = Checkbutton(frame4, variable=checkBoxVal, text = 'Extra ost')
checkBox2.pack(side=LEFT)
checkBoxVal = StringVar()
checkBox2 = Checkbutton(frame4, variable=checkBoxVal, text = 'Hvítlaukssósu')
checkBox2.pack(side=LEFT)

button1=Button(frame5, padx=20, pady=7, bd=8, fg='Black', text='Panta Pizzu', command=pontun)
button1.pack(padx = 5)
button1.config(height=1, width=2)
