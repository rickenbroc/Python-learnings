from tkinter import *
import random
import time

class Jeu:
    def __init__(self) -> None:
        self.tk = Tk()
        self.tk.title("M. Filiforme court vers la sortie")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, \
                              highlightthickness=0)
        self.canvas.pack()
        self.canvas.update()
        self.hauteur_canevas = 500
        self.largeur_canevas = 500
        self.ap = PhotoImage(file="Filiforme\\arriere-plan.gif")
        larg = self.ap.width()
        haut = self.ap.height()
        for x in range(0, 5):
                for y in range(0, 5):
                    self.canvas.create_image(x * larg, y * haut, \
                                             image=self.ap, anchor = 'nw')
        self.lutins = []
        self.enfonction = True

    def boucle_principale(self):
         while 1:
              if self.enfonction == True:
                    for lutin in self.lutins:
                        lutin.deplacer()
                    self.tk.update_idletasks()
                    self.tk.update()
                    time.sleep(0.01)

class Coords:
     def __init__(self, x1=0, y1=0, x2=0, y2=0) -> None:
          self.x1 = x1
          self.y1 = y1
          self.x2 = x2
          self.y2 = y2

class Lutin:
     def __init__(self, jeu) -> None:
          self.jeu = jeu    # pour pouvoir accéder aux autres lutins
          self.finjeu = False
          self.coordonnees = None   #mémoriser la position du lutin

     def deplacer(self):
          pass
     
     def coords(self):
          return self.coordonnees

class LutinPlateforme(Lutin):
     def __init__(self, jeu, image_photo, x, y, largeur, hauteur) -> None:
          Lutin.__init__(self, jeu)
          self.image_photo = image_photo
          self.image = jeu.canvas.create_image(x, y, \
                                               image=self.image_photo, anchor='nw')
          self.coordonnees = Coords(x, y, x + largeur, y + hauteur)


def dans_x(co1, co2):
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
    or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
    or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
    or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
         return True
    else:
        return False

def dans_y(co1, co2):
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
    or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
    or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
    or (co2.y2 > co1.y1 and co2.y2 < co1.y2):
         return True
    else:
        return False

def collision_gauche(co1, co2):
    if dans_y(co1, co2):   #co1 dans co2 verticalement
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:  #coté gauche de co1 dans co2 horizontalemnt
            return True
    return False

def collision_droite(co1, co2):
    if dans_y(co1, co2):
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
            return True
    return False
          
def collision_haut(co1, co2):
     if dans_x(co1,co2):
          if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
               return True
     return False

def collision_bas(y, co1, co2):
     if dans_x(co1, co2):
          y_calc = co1.y2 + y
          if y_calc >= co2.y1 and y_calc <= co2.y2:
               return True
     return False

jeu=Jeu()

plateforme1 = LutinPlateforme(jeu, PhotoImage(file='Filiforme/plate-forme1.gif'), 0, 480, 100, 10)
plateforme2 = LutinPlateforme(jeu, PhotoImage(file='Filiforme/plate-forme1.gif'), 150, 440, 100, 10)
plateforme3 = LutinPlateforme(jeu, PhotoImage(file='Filiforme/plate-forme1.gif'), 300, 400, 100, 10)
plateforme4 = LutinPlateforme(jeu, PhotoImage(file='Filiforme/plate-forme1.gif'), 300, 160, 100, 10)
plateforme5 = LutinPlateforme(jeu, PhotoImage(file='Filiforme/plate-forme2.gif'), 175, 350, 66, 10)
plateforme6 = LutinPlateforme(jeu, PhotoImage(file='Filiforme/plate-forme2.gif'), 50, 300, 66, 10)
plateforme7 = LutinPlateforme(jeu, PhotoImage(file='Filiforme/plate-forme2.gif'), 170, 120, 66, 10)
plateforme8 = LutinPlateforme(jeu, PhotoImage(file='Filiforme/plate-forme2.gif'), 45, 60, 66, 10)
plateforme9 = LutinPlateforme(jeu, PhotoImage(file='Filiforme/plate-forme3.gif'), 170, 250, 32, 10)
plateforme10 = LutinPlateforme(jeu, PhotoImage(file='Filiforme/plate-forme3.gif'), 230, 200, 32, 10)

jeu.boucle_principale()

                   