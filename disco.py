import random
from Tkinter import *
root = Tk()

temp = None


def leftClick(event):
    global temp
    randColor = random.randint(0, 2)
    if temp == 0:
        randColor = random.randint(1, 2)
    elif temp == 1:
        randColor = random.randrange(0, 2, 2)
    elif temp == 2:
        randColor = random.randint(0, 1)

    if randColor == 0:
        frame.configure(background='blue')
        temp = 0
    if randColor == 1:
        frame.configure(background='purple')
        temp = 1
    if randColor == 2:
        frame.configure(background='red')
        temp = 2


frame = Frame(root, width=500, height=250)
frame.bind("<Button-1>", leftClick)
frame.pack()

root.mainloop()
