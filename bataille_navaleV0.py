from tkinter import *

fenetre = Tk()

for row in range(1, 6):
    for column in range(1, 6):
        Button(fenetre, text=str(row) + " ; " +
               str(column), bg='white').grid(row=row, column=column)


fenetre.mainloop()
