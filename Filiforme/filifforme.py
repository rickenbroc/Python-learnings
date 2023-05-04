### imports
from tkinter import *
import random
import time

### Classes
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
        self.texte_fin_partie = self.canvas.create_text(250, 250, text="Tu as gagné !", state="hidden")
        self.ap = PhotoImage(file="Filiforme/arriere-plan.gif")
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
              else:
                   time.sleep(1)
                   self.canvas.itemconfig(self.texte_fin_partie, state='normal')
                   
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

class LutinPersonnage(Lutin):
     def __init__(self, jeu) -> None:
          Lutin.__init__(self, jeu)
          self.images_gauche = [PhotoImage(file='Filiforme/fil-G1.gif'), PhotoImage(file='Filiforme/fil-G2.gif'), PhotoImage(file='Filiforme/fil-G3.gif')]
          self.images_droite = [PhotoImage(file='Filiforme/fil-D1.gif'), PhotoImage(file='Filiforme/fil-D2.gif'), PhotoImage(file='Filiforme/fil-D3.gif')]
          self.image = jeu.canvas.create_image(200, 470, image=self.images_gauche[0], anchor='nw')
          self.x = -2   #déplacement à gauche
          self.y = 0
          self.image_courante = 0   # indice de l'image en cours d'affichage
          self.ajout_image_courante = 1 # prochaine image
          self.compte_sauts = 0
          self.derniere_heure = time.time() # mémorise la ls dernière fois que l'image a changé pendant l'animation du personnage
          self.coordonnees = Coords()
          jeu.canvas.bind_all('<KeyPress-Left>', self.tourner_a_gauche)
          jeu.canvas.bind_all('<KeyPress-Right>', self.tourner_a_droite)
          jeu.canvas.bind_all('<space>', self.sauter)
 
     def tourner_a_gauche(self, evt):
          #si le perso n'est pas en train de sauter ou de tomber
          if self.y == 0:
               self.x = -2

     def tourner_a_droite(self, evt):
          if self.y == 0:
               self.x = 2
     
     def sauter(self, evt):
          if self.y == 0:
               self.y = -4
               self.compte_sauts = 0   # gestion de la gravité, ne peux pas sauter à l'infini

     def animer(self):
          if self.x !=0 and self.y == 0:
               if time.time() - self.derniere_heure > 0.1:
                    self.derniere_heure = time.time()
                    self.image_courante += self.ajout_image_courante
                    if self.image_courante >= 2:
                         self.ajout_image_courante = -1
                    if self.image_courante < 0:
                         self.ajout_image_courante = 1
          if self.x < 0:
               if self.y != 0:
                    self.jeu.canvas.itemconfig(self.image, image=self.images_gauche[2])
               else:
                    self.jeu.canvas.itemconfig(self.image, image=self.images_gauche[self.image_courante])
          elif self.x > 0:
               if self.y != 0:
                    self.jeu.canvas.itemconfig(self.image, image=self.images_droite[2]) 
               else:
                    self.jeu.canvas.itemconfig(self.image, image=self.images_droite[self.image_courante]) 
     
     def coords(self):
          xy = self.jeu.canvas.coords(self.image)
          self.coordonnees.x1 = xy[0]
          self.coordonnees.y1 = xy[1]
          self.coordonnees.x2 = xy[0] + 27
          self.coordonnees.y2 = xy[1] + 30
          return self.coordonnees
     
     def deplacer(self):
          self.animer()
          if self.y < 0: # le personnage monte
               self.compte_sauts += 1
               if self.compte_sauts > 20:
                    self.y = 4 # et redescend
          if self.y > 0:
               self.compte_sauts -= 1
          co = self.coords()
          gauche = True
          droite = True
          haut = True
          bas = True
          tombe = True
          
          # le personnage a-t-il touché le bas ou le haut du canevas ?
          if self.y > 0 and co.y2 >= self.jeu.hauteur_canevas:   # tombe
               self.y = 0
               bas = False #tout en bas, plus besoin de vérifier
          elif self.y < 0 and co.y1 <= 0:                        #saute
               self.y = 0
               haut = False # tout en haut, plus besoin de vérifier
          
          # le personnage a-t-il touché un côté du canevas ?
          if self.x > 0 and co.x2 >= self.jeu.largeur_canevas:
               self.x = 0
               droite = False
          if self.x < 0 and co.x1 <= 0:
               self.x = 0
               gauche = False
          
          # collisions avec d'autres lutins
          for lutin in self.jeu.lutins:
               if lutin == self:   # si le lutin est l'objet courant
                    continue       # passer au suivant
               co_lutin = lutin.coords()
               
               # collision en haut
               if haut and self.y < 0 and collision_haut(co, co_lutin): # en montée, pas en haut, en collision avec co_lutin
                    self.y = -self.y    # sens inverse
                    haut = False 

               # collision en bas
               if bas and self.y > 0 and collision_bas(self.y, co, co_lutin):
                    self.y = co_lutin.y1 - co.y2  # compensation en pixel de la distance au point d'impact
                    if self.y < 0:                # si négatif alors 0 pour ne pas rebondir
                         self.y = 0
                    bas = False
                    haut = False

               # drapeau bas = true
               # peut tomber
               # n'est pas déjà en train de tomber
               # bas du perso plus haut que le bord inférieur du canevas
               # le perso touche une plateforme
               #    alors arrête de tomber

               if bas and tombe \
               and self.y == 0 \
               and co.y2 < self.jeu.hauteur_canevas \
               and collision_bas(1, co, co_lutin):
                    tombe = False
               
               # vérifier la gauche et la droite
               if gauche and self.x < 0 and collision_gauche(co, co_lutin):
                    self.x = 0
                    gauche = False
                    if lutin.finjeu:
                         # si finjeu = true alors lutin est la porte
                         self.fin(lutin)
                         
               if droite and self.x > 0 and collision_droite(co, co_lutin):
                    self.x = 0
                    droite = False
                    if lutin.finjeu:
                         self.fin(lutin)
                        

          if tombe and bas and self.y ==0 and co.y2 < self.jeu.hauteur_canevas:
               self.y = 4
          self.jeu.canvas.move(self.image, self.x, self.y)
          
     def fin(self, lutin):
          self.jeu.enfonction = False
          lutin.ouvrir_porte()
          time.sleep(1)
          self.jeu.canvas.itemconfig(self.image, state='hidden')
          lutin.fermer_porte()


               
class LutinPorte(Lutin):
     def __init__(self, jeu, x, y, largeur, hauteur) -> None:
          super().__init__(jeu)
          self.porte_fermee = PhotoImage('Filiforme/porte1.gif')
          self.porte_ouverte = PhotoImage("filiforme/porte2.gif")
          self.image = jeu.canvas.create_image(x, y, image=self.porte_fermee, anchor='nw')
          self.coordonnees= Coords(x, y, x + largeur / 2, y + hauteur)
          self.finjeu = True
     
     def ouvrir_porte(self):
          jeu.canvas.itemconfig(self.image, image = self.porte_ouverte)
          self.jeu.tk.update_idletasks()
          
     def fermer_porte(self):
          jeu.canvas.itemconfig(self.image, image = self.porte_fermee)
          self.jeu.tk.update_idletasks()
          
### fonctions           
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

### Programme principal
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

# rajout à la liste des lutins
jeu.lutins.append(plateforme1)
jeu.lutins.append(plateforme2)
jeu.lutins.append(plateforme3)
jeu.lutins.append(plateforme4)
jeu.lutins.append(plateforme5)
jeu.lutins.append(plateforme6)
jeu.lutins.append(plateforme7)
jeu.lutins.append(plateforme8)
jeu.lutins.append(plateforme9)
jeu.lutins.append(plateforme10)

# rajout M.Filiforme
personnage = LutinPersonnage(jeu)
jeu.lutins.append(personnage)

# rajout Porte de sortie
porte = LutinPorte(jeu, 45, 30, 40, 35)
jeu.lutins.append(porte)

jeu.boucle_principale()
