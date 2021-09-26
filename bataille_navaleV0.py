from tkinter import *
from functools import partial
from random import *
from Boat import Boat
from State import States
from time import sleep
import tkinter.font as tkFont

boatlist = []
for i in range(2):
    boat = Boat(randint(1, 6), randint(1, 6))
    if i > 0:
        for ent in boatlist:
            if boat == ent:
                boat = Boat(randint(1, 6), randint(1, 6))
    boatlist.append(boat)

counter = 0


fenetre = Tk()
fenetre.geometry("800x515")

font = tkFont.Font(family="Arial", size=16, weight="bold")

grid = Frame(fenetre, height=515, width=515)
grid.pack(side="left")

def init():
    for row in range(1, 7):
        for column in range(1, 7):
            Button(grid, bg='white', command=partial(
                Clicked, row, column), height=5, width=10).grid(row=row, column=column)

text = StringVar()
text.set("Nombre d'essais : " + str(counter))

textframe = Frame(fenetre)
textframe.pack(side="right")

tryc = Label(textframe, width=30, height=5, bd=5, textvariable=text, font=font)
tryc.pack(side="top")

def retry():
    global counter
    counter = 0
    text.set("Nombre d'essais : " + str(counter))
    for boat in boatlist:
        boat.setState(States.Alive)
    init()

retry = Button(textframe, command=retry, text="Réessayer")
retry.pack()

def quit():
    fenetre.destroy()

quit = Button(textframe, command=quit, text="Quitter")
quit.pack()

def areAllAlive():
    k = 0
    for boat in boatlist:
        if boat.isAlive():
            k += 1
    if k > 0:
        return True
    else:
        return False

def Clicked(x, y):
    global counter
    if areAllAlive(): counter +=1
    text.set("Nombre d'essais : " + str(counter))
    a = 0
    for boat in boatlist:
        if boat.state == States.Dead:
            print("Coulé !")
        elif boat.x == x and boat.y == y:
            print("FOUND")
            boat.setState(States.Dead)
            Button(grid, bg='red', height=5, width=10).grid(row=x, column=y)
            a = 1
            print("Coulé !")
        elif boat.x == x or boat.y == y:
            for boatb in boatlist:
                if boatb.x == x and boatb.y == y:
                    Button(grid, bg='red', height=5,
                           width=10).grid(row=x, column=y)
                    a = 1
            if a == 0:
                Button(grid, bg='orange', height=5,
                       width=10).grid(row=x, column=y)
                print("En vue !")
        else:
            if a == 0:
                Button(grid, bg='blue', height=5,
                       width=10).grid(row=x, column=y)
            print("A l'eau !")

    if areAllAlive() == False:
        print("Bravo ! Vous avez coulé tous les navires !")

init()

fenetre.mainloop()
