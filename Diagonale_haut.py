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

assert diag_haut([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0]],1,5,2)== True
assert diag_haut([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]],1,5,2)==False