#3.1
def grille_vide():
    return [[0 for i in range(7)] for j in range(6)]

assert grille_vide()== [[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]
assert len(grille_vide()) == 6
assert len(grille_vide()[1]) == 7