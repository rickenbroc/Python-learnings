from tkinter import *
from tkinter import colorchooser
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

mon_triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0,60):
    canvas.move(mon_triangle, 5, 4) 
    tk.update()
    time.sleep(0.05)

for x in range(0,60):
    canvas.move(mon_triangle, -5,-4)
    tk.update()
    time.sleep(0.01)
