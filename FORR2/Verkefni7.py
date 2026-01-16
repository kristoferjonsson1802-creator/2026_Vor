from tkinter import *
import tkinter.messagebox

import random

deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4

p1_hand = []
p2_hand = []

p1_done = False
p2_done = False

def draw_card(hand):
    card = random.choice(deck)
    hand.append(card)

def hand_value(hand):
    total = sum(hand)
    aces = hand.count(11)

    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def p1_draw():
    global p1_done
    if not p1_done:
        draw_card(p1_hand)
        p1_stig.set(str(hand_value(p1_hand)))
        if hand_value(p1_hand) >= 21:
            p1_done = True
            check_winner()

def p1_stop():
    global p1_done
    p1_done = True
    check_winner()

def p2_draw():
    global p2_done
    if not p2_done:
        draw_card(p2_hand)
        p2_stig.set(str(hand_value(p2_hand)))
        if hand_value(p2_hand) >= 21:
            p2_done = True
            check_winner()

def p2_stop():
    global p2_done
    p2_done = True
    check_winner()

def check_winner():
    if not (p1_done and p2_done):
        return

    p1 = hand_value(p1_hand)
    p2 = hand_value(p2_hand)

    if p1 > 21 and p2 > 21:
        msg = "Báðir sprungu"
    elif p1 > 21:
        msg = "Spilari 2 vinnur"
    elif p2 > 21:
        msg = "Spilari 1 vinnur"
    elif p1 > p2:
        msg = "Spilari 1 vinnur "
    elif p2 > p1:
        msg = "Spilari 2 vinnur"
    else:
        msg = "Jafntefli"

    tkinter.messagebox.showinfo("Niðurstaða", msg)

def reset_game():
    global p1_hand, p2_hand, p1_done, p2_done

    p1_hand = []
    p2_hand = []
    p1_done = False
    p2_done = False

    p1_stig.set("")
    p2_stig.set("")
    
    labelText.set("Byrjaðu að spila       Byrjaðu að spila")
    
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

p1_stig = StringVar()
p1_stiginn = Entry(frame2, textvariable=p1_stig)
p1_stiginn.pack(side=LEFT, padx=15)

p2_stig = StringVar()
p2_stiginn = Entry(frame2, textvariable=p2_stig)
p2_stiginn.pack(side=LEFT, padx=15)


button1=Button(frame3, padx=20, pady=7, bd=8, fg='Black', text='Draga spil', command=p1_draw)
button1.pack(side=LEFT, padx = 5)
button1.config(height=1, width=2)
button2=Button(frame3, padx=20, pady=7, bd=8, fg='Black', text='Hætta', command=p1_stop)
button2.pack(side=LEFT, padx = 5)
button2.config(height=1, width=2)

button3=Button(frame3, padx=20, pady=7, bd=8, fg='Black', text='Draga spil', command=p2_draw)
button3.pack(side=LEFT, padx = 5)
button3.config(height=1, width=2)
button4=Button(frame3, padx=20, pady=7, bd=8, fg='Black', text='Hætta', command=p2_stop)
button4.pack(side=LEFT, padx = 5)
button4.config(height=1, width=2)

button5=Button(frame4, padx=40, pady=7, bd=8, fg='Black', text='Byrja upp á nýtt', command=reset_game)
button5.pack(side=LEFT)
button5.config(height=1, width=2)

