from tkinter import *
import tkinter.messagebox

def beenClicked():
    radioValue = relStatus.get()
    print (radioValue)
    tkinter.messagebox.showinfo('þú ýttir á', radioValue)
    return #endar fallið

def changeLabel():
    name = ('Takk fyrir að smella ' + yourName.get())
    labelText.set(name)
    yourName.delete(0, END)
    yourName.insert(0, 'Ég heiti Kristófer')

#forrit byrjar
gluggi = Tk() #býr til glugga 
gluggi.title('Verkefni 1') #gefir glugga nafn
gluggi.geometry('450x300+100+100') #fyrstu tölur er stærð  #seinni er hvar gluggi er 

#Býr til Label
labelText = StringVar()
labelText.set('Sýnidæmi')
labell = Label(gluggi, textvariable=labelText, height=4) 
labell.pack() #birtir á skjæainn

#checkbox
checkBoxVal = IntVar()
checkBox1 = Checkbutton(gluggi, variable=checkBoxVal, text = 'þetta er checkbox')
checkBox1.pack() #birtir á skjæainn

#input box
custName = StringVar(None) #enginn texti sem er í byrjuninni á boxinu
yourName = Entry(gluggi, textvariable=custName) #býr til entry box
yourName.pack() #birtir á skjæainn

#býr til Radiobutton
relStatus = StringVar()
relStatus.set(None)
radio1 = Radiobutton(gluggi, text='Einhleypur', value='Einhleypur', variable = relStatus, command = beenClicked).pack()
radio1 = Radiobutton(gluggi, text='Giftur', value='Giftur', variable = relStatus, command = beenClicked).pack()

#býr til button
button1 = Button(gluggi, text='Smelltu hér', width=20, command=changeLabel)
button1.pack(side='bottom', padx = 15, pady = 15)

gluggi.mainloop() #loopa þannig að forritð hætir ekki
