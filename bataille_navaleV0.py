from tkinter import *
from functools import partial
from random import *
from Boat import Boat
from State import States
from time import sleep

boatlist = []
for i in range(2):
    boat = Boat(randint(1, 6), randint(1, 6))
    print(boat.x, boat.y)
    if i > 0:
        for ent in boatlist:
            if boat == ent:
                boat = Boat(randint(1, 6), randint(1, 6))
    boatlist.append(boat)


fenetre = Tk()


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
    a = 0
    for boat in boatlist:
        print(boat.x, " --> ", x)
        print(boat.y, " --> ", y)
        if boat.state == States.Dead:
            print("Coulé !")
        elif boat.x == x and boat.y == y:
            print("FOUND")
            boat.setState(States.Dead)
            Button(fenetre, bg='red', height=5, width=10).grid(row=x, column=y)
            a = 1
            print("Coulé !")
        elif boat.x == x or boat.y == y:
            for boatb in boatlist:
                print(" ")
                print(boatb.x, " -> ", x)
                print(" ")

                print(" ")
                print(boatb.y, " -> ", y)
                print(" ")
                if boatb.x == x and boatb.y == y:
                    Button(fenetre, bg='red', height=5,
                           width=10).grid(row=x, column=y)
                    a = 1
            if a == 0:
                Button(fenetre, bg='orange', height=5,
                       width=10).grid(row=x, column=y)
                print("En vue !")
        else:
            if a == 0:
                Button(fenetre, bg='blue', height=5,
                       width=10).grid(row=x, column=y)
            print("A l'eau !")

    if areAllAlive() == False:
        print("Stonks")
        fenetre.quit()
        print("Bravo ! Vous avez coulé tous les navires !")


for row in range(1, 7):
    for column in range(1, 7):
        Button(fenetre, bg='white', command=partial(
            Clicked, row, column), height=5, width=10).grid(row=row, column=column)


fenetre.mainloop()
