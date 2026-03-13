from tkinter import *

def donothing():
    x=0
window=Tk()
menubar=Menu(window)

filemenu=Menu (menubar,tearoff=0)

menubar.add_cascade(label='filename',menu=filemenu)
filemenu.add_command(label='new',command=donothing)
filemenu.add_command(label='open',command=donothing)
filemenu.add_command(label='save',command=donothing)
filemenu.add_separator()
filemenu.add_command(label='exit',command=donothing)

helpmenu =Menu(menubar,tearoff=1)
menubar.add_cascade(label='help',menu=helpmenu)
helpmenu.add_command(label='help index', command=donothing)
helpmenu.add_command(label='about...',command=donothing)

window.config(menu=menubar)

window.mainloop()