from tkinter import *
from tkinter import colorchooser
import random

tk=Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

def creer_triangle_aleatoire():
    x1 = random.randint(0,random.randint(0,500))                #entre 0 et aléatoire 0-500
    y1 = random.randint(0,random.randint(0,500))
    x2 = min(500, x1 + random.randint(0,random.randint(0,500))) #min pour ne pas dépasser le canvas
    y2 = min(500, y1 + random.randint(0,random.randint(0,500)))
    x3 = min(500, x1 + random.randint(0,random.randint(0,500)))
    y3 = min(500, y1 + random.randint(0,random.randint(0,500)))
    r = '%02x' % random.randint(0,128)                          # aleatoire en hexa sur deux caractères
    v = '%02x' % random.randint(0,128)
    b = '%02x' % random.randint(0,128)
    couleur = '#'+r+v+b                                         #code couleur du triangle
    return canvas.create_polygon(x1,y1,x2,y2,x3,y3, fill=couleur)

for i in range(1, 50):
    print(creer_triangle_aleatoire())

