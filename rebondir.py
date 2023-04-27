from tkinter import *
import time
import random

class Balle:
    def __init__(self, canvas, raquette, score, couleur):
        self.canvas = canvas
        self.raquette = raquette
        self.score = score
        self.id = canvas.create_oval(10 , 10, 25, 25, fill=couleur)
        self.canvas.move(self.id, 245, 100) #place au centre
        departs = [-3, -2, -1, 1, 2 , 3]
        random.shuffle(departs)
        self.x = departs[0]
        self.y = -3
        self.hauteur_canevas = self.canvas.winfo_height()   #hauteur du canevas
        self.largeur_canevas = self.canvas.winfo_width()    #largeur du canevas
        self.touche_bas = False
        self.demarre_jeu = False
        self.canvas.bind_all('<Button-1>', self.demarrer_jeu)
        self.texte_debut = self.canvas.create_text(200, 200, text="Cliquer pour commencer")

    def demarrer_jeu(self, evt):
        self.demarre_jeu = True
        self.canvas.itemconfig(self.texte_debut, state='hidden')

    def heurter_raquette(self, pos):
        pos_raquette = self.canvas.coords(self.raquette.id)
        if pos[2] >= pos_raquette[0] and pos[0]<= pos_raquette[2]:
            if pos[3] >= pos_raquette[1] and pos[3] <= pos_raquette[3]:
                self.x += self.raquette.x
                self.score.incrementer_score()
                return True
        return False
        

    def dessiner(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)   #position actuelle de l'objet liste[x1,y1,x2,y2]
        if pos[1] <= 0: # y1 bord supérieur de l'objet plus haut que le bord du canvas
            self.y = 3  # changement de sens
        if pos[3] >= self.hauteur_canevas: #y2 bord inférieur de l'objet
            self.y = -3 
        if pos[0] <= 0: # bord gauche de la balle touche le bord gauche du canevas
            self.x = 3 # repart à droite
        if pos[2] >= self.largeur_canevas:  #bord droit de la balle touche le bord droit
            self.x = -3 # repart à gauche
        if self.heurter_raquette(pos) == True:  # touche la raquette
            self.y = -3                     # repart vers le haut
        if pos[3] >= self.hauteur_canevas:
            self.touche_bas = True
  

class Raquette:
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=couleur)
        self.canvas.move(self.id, 200, 300)
        self.largeur_canevas = self.canvas.winfo_width()
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.vers_gauche)
        self.canvas.bind_all('<KeyPress-Right>', self.vers_droite)

    def vers_gauche(self, evt):
        self.x = -2

    def vers_droite(self, evt):
        self.x = 2
    
    def dessiner(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.largeur_canevas:
            self.x = 0

class Score:
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.score = 0
        self.id = canvas.create_text(300, 10, text="Score : %s points" % self.score, fill=couleur)

    def incrementer_score(self):
        self.score += 1
        canvas.itemconfig(self.id,  text="Score : %s points" % self.score)

### initialisation
tk = Tk()
tk.title("Jeu Rebondir")     #titre de fenêtre
tk.resizable(0, 0)  #bloque le redimensionnement x,y
tk.wm_attributes("-topmost", 1) #fenêtre au premier plan
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)  #fenêtre sans bordures
canvas.pack()       #applique les paramètres
tk.update()         #initialise tkinter pour l'animation du jeu

texte_fin = canvas.create_text(200, 200, text="Partie terminée !", state='hidden')
score = Score(canvas, 'green')
raquette = Raquette(canvas, 'blue')
balle = Balle(canvas, raquette, score, 'red')    # creation de l'objet balle

### Boucle principale
while 1:
    if balle.touche_bas == False and balle.demarre_jeu == True:
        raquette.dessiner()
        balle.dessiner()
    if balle.touche_bas == True:
        canvas.itemconfig(texte_fin, state='normal')
        
    tk.update_idletasks()   #redessiner rapidement evts systemes
    tk.update()             #autres evts
    time.sleep(0.01)
