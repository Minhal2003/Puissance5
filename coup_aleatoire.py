from random import*
def coup_aleatoire(gril ,j):
    p = randint(0,6)
    u = Jouer (gril, j, col)
    return u

coup_aleatoire(grille_vide(),2)