from tkinter import *
import tkinter.messagebox

gluggi = Tk()
gluggi.title('TicTacToe')
gluggi.geometry('450x350')

frame0 = Frame(gluggi)
frame0.pack(side = TOP)
frame1 = Frame(gluggi)
frame1.pack(side = TOP)
frame2 = Frame(gluggi)
frame2.pack(side = TOP)
frame3 = Frame(gluggi)
frame3.pack(side = TOP)

labelText = StringVar()
labelText.set('TicTacToe')
labell = Label(frame0, textvariable=labelText, height=4, font=('arial', 12, 'bold')) 
labell.pack()

red_turn = True

def on_click(button):
    global red_turn

    if red_turn:
        button.config(bg="red")
    else:
        button.config(bg="blue")

    button.config(state=DISABLED)
    red_turn = not red_turn


button1=Button(frame1, padx=20, pady=20, bd=8, fg='Black', bg='White', command=lambda: on_click(button1))
button1.pack(side=LEFT)
button1.config(height=1, width=2)
button2=Button(frame1, padx=20, pady=20, bd=8, fg='Black', bg='White', command=lambda: on_click(button2))
button2.pack(side=LEFT)
button2.config(height=1, width=2)
button3=Button(frame1, padx=20, pady=20, bd=8, fg='Black', bg='White', command=lambda: on_click(button3))
button3.pack(side=LEFT)
button3.config(height=1, width=2)

button4=Button(frame2, padx=20, pady=20, bd=8, fg='Black', bg='White', command=lambda: on_click(button4))
button4.pack(side=LEFT)
button4.config(height=1, width=2)
button5=Button(frame2, padx=20, pady=20, bd=8, fg='Black', bg='White', command=lambda: on_click(button5))
button5.pack(side=LEFT)
button5.config(height=1, width=2)
button6=Button(frame2, padx=20, pady=20, bd=8, fg='Black', bg='White', command=lambda: on_click(button6))
button6.pack(side=LEFT)
button6.config(height=1, width=2)

button7=Button(frame3, padx=20, pady=20, bd=8, fg='Black', bg='White', command=lambda: on_click(button7))
button7.pack(side=LEFT)
button7.config(height=1, width=2)
button8=Button(frame3, padx=20, pady=20, bd=8, fg='Black', bg='White', command=lambda: on_click(button8))
button8.pack(side=LEFT)
button8.config(height=1, width=2)
button9=Button(frame3, padx=20, pady=20, bd=8, fg='Black', bg='White', command=lambda: on_click(button9))
button9.pack(side=LEFT)
button9.config(height=1, width=2)
