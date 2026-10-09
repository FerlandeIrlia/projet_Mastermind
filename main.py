import pygame
import random
import mm


Nombre_PION = 5
Nombre_ESSEAI = 15

# Initialisation de pygame
pygame.init()

def generesSecret () -> list :
   secret = []
   for couleur in range(0,Nombre_PION):
      couleur = random.choice(mm.TabCouleur)
      secret.append(couleur)
   return secret

def nombreBiePlace (prop:list,secret:list) -> list :
   nombre  = 0
   for i in range(Nombre_PION) :

      if secret[i] == prop[i] :
         nombre +=nombre
   return nombre

def nombrePionMaPlacee () :
   Pion_commun = 0
   for couleur in mm.TabCouleur :
      Pion_commun = 



      


# Création de la fenêtre
fenetre = pygame.display.set_mode((800, 700))
pygame.display.set_caption("MasterMind")

# Affichage de l'interface
fenetre.fill((255,255,255))
mm.afficherPlateau(fenetre)
pygame.display.update()

# Génération aléatoire de la combinaison secrète
secret = []


# Boucle principale du jeu
for ligne in range(1, nombre_lignes + 1):

    # Le joueur construit sa proposition
    proposition = mm.construireProposition(fenetre, ligne)

    # Calcul du résultat
    resultat = mm.distance(secret, proposition)

    # Affichage du résultat
    mm.afficherResultat(fenetre, resultat, ligne)

    # Actualisation de la fenêtre
    pygame.display.update()

    # Vérification de la victoire
    if resultat[0] == 5:
      gagne = True
      print("Vous avez gagné !")
      break


# Si le joueur n'a pas trouvé la combinaison
if not gagne:
   print("Vous avez perdu !")
   print("La combinaison secrète était :", secret)

# Boucle permettant de garder la fenêtre ouverte
ferme = False

while not ferme:
   for evenement in pygame.event.get():

    if evenement.type == pygame.QUIT:
     ferme = True

pygame.quit()
