from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

def affiche_touche(evenement):
    print(evenement.keysym)

canvas.bind_all('<KeyPress>', affiche_touche)
