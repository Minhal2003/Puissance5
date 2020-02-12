def grille_vide():
    return [[0 for i in range(7)] for j in range(6)]

def affiche(gril):
    print(" 0","1","2","3","4","5","6")
    for i in gril:
        for j in i :
            if j == 0:
                print("|.",end="")
            elif j == 1:
                print("|x",end="")
            elif j == 2:
                print("|0",end="")
        print('|')

def coup_possible(gril,col):
    if gril[0][col]==0:
        return True
    else:
        return False

def jouer(gril,j,col):
    p=0
    for i in range(6):
        if gril[5-i][col]==0 and p==0:
            gril[5-i][col]=j
            p+=1
    return gril

def horiz (gril, j, lig, col):
    compteur=0
    if lig>5:
        return False
    if col>3:
        return False
    for i in range(4):
        if gril[lig][col+i]==j:
            compteur+=1
    if compteur==4:
            return True
    return False

def vert(gril,j,lig,col):
    k=0
    if lig>3:
        return False
    for i in range(lig+1,lig+3):
        if gril[i][col]!=j:
            k=1
    if k==1:
        return False
    else:
        return True
    
def diag_haut(gril, j, lig, col):
    p=0
    if lig<4:
        return False
    if col>2:
        return False
    for i in range(4):
        if gril[lig-i][col+i]==j:
            p+=1
    if p==4:
            return True
    return False

def diag_bas(gril, j, lig, col):
    p=0
    if lig>3:
        return False
    if col>2:
        return False
    for i in range(4):
        if gril[lig+i][col+i]==j:
            p+=1
    if p==4:
            return True
    return False

def victoire(gril,j ,lig , col):
    if horiz(gril,j,lig , col)==True or diag_bas(gril,j,lig,col)==True or diag_bas(gril, j, lig, col)==True or vert(gril,j,lig,col) :
        return True
    else:
        return False
    
def match_nul(gril):
    for i in range(7):
        for z in range(6):
            if gril[z][i]==0:
                return False
    return True

from random import*
def coup_aleatoire(gril ,j):
    p = randint(0,6)
    u = Jouer (gril, j, p)
    return u

# Programme principal

L = grille_vide()
affiche(L)
n = int(input("Quelle colonne jouer vous ?"))

L = jouer(L,1,n)
affiche(L)
