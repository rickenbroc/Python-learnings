from tkinter import *
from tkinter import colorchooser
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

mon_triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
def bouger_triangle(evenement):
    if evenement.keysym == 'Up':
        canvas.move(mon_triangle, 0, -3)
    elif evenement.keysym == 'Down':
        canvas.move(mon_triangle, 0, 3)
    elif evenement.keysym == 'Left':
        canvas.move(mon_triangle, -3, 0)
    elif evenement.keysym == 'Right':
        canvas.move(mon_triangle, 3, 0)
    else:
        print('Hein?')

canvas.bind_all('<KeyPress-Up>', bouger_triangle)
canvas.bind_all('<KeyPress-Down>', bouger_triangle)
canvas.bind_all('<KeyPress-Left>', bouger_triangle)
canvas.bind_all('<KeyPress-Right>', bouger_triangle)
