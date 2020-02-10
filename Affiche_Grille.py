#3.2
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
        
affiche([[1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 2, 0, 0, 0],
 [0, 0, 0, 2, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 2, 0, 0]]) 