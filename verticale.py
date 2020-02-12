def vert(gril,j,lig,col):
    p=0
            if lig>3:
            return False
    for i in range(lig+1,lig+3):
        if gril[i][col]!=j:
            p=1
    if p==1:
        return False
    else:
        return True
        
assert vert([[0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 2, 0, 0, 0, 0],
      [0, 0, 2, 0, 0, 0, 0]],1,2,2)==False