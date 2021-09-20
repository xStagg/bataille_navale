from State import States


class Boat:
    def __init__(self, x,  y):
        self.x = x
        self.y = y
        self.state = States.Alive

    def setState(self, state):
        self.state = state

    def isAlive(self):
        if self.state == States.Alive:
            return True
        else:
            return False
