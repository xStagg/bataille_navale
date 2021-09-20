from random import *
from Boat import Boat
from State import States

boatlist = []
for i in range(2):
    boat = Boat(randint(1, 6), randint(1, 6))
    print(boat.x, boat.y)
    if i > 0:
        for ent in boatlist:
            if boat == ent:
                boat = Boat(randint(1, 6), randint(1, 6))
    boatlist.append(boat)


def areAllAlive():
    k = 0
    for boat in boatlist:
        if boat.isAlive():
            k += 1
    if k > 0:
        return True
    else:
        return False


while areAllAlive():

    x = int(input("Colonne : "))
    y = int(input("Ligne : "))

    for boat in boatlist:
        if boat.state == States.Dead:
            print("Coulé !")
        elif boat.x == x and boat.y == y:
            boat.setState(States.Dead)
            print("Coulé !")
        elif boat.x == x or boat.y == y:
            print("En vue !")
        else:
            print("A l'eau !")

print("Bravo ! Vous avez coulé tous les navires !")
