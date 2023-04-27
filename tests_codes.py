from tkinter import *
from tkinter import colorchooser
import random
tk = Tk(screenName='dessin')
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

def rectangle_aleatoire(largeur, hauteur, coul_rempl):
    x1 = random.randrange(largeur)
    y1 = random.randrange(hauteur)
    x2 = min(x1 + random.randrange(largeur), 500)
    y2 = min(y1 + random.randrange(hauteur), 500)
    canvas.create_rectangle(x1, y1, x2, y2, fill=coul_rempl)
    print("x1 %s, y1 %s, x2 %s, y2 %s" %(x1,y1,x2,y2))


#c = colorchooser.askcolor()
#rectangle_aleatoire(400,400, c[1])

canvas.create_arc(10,10,200,100, extent=180, style=ARC)
canvas.create_text(150, 100, text='Soyez plutôt maçon')
canvas.create_text(170, 120, text="Si c'est votre talent", fill='red')
canvas.create_text(200, 150, text="bla bla", fill='blue', font=('Times', 20))

#images
mon_image = PhotoImage(file='c:\\temp\\m3.gif')
canvas.create_image(0,0, anchor=NW, image=mon_image)

