L =[[1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0],
 [1,0,0,0,0,0,0],
 [1,0,0,0,0,0,0],
 [1,1,2,0,0,0,0],
 [1,1,2,2,2,0,0]
]
def coup_possible(gril,col):
    if gril[0][col]==0:
        return True
    else:
        return False
    
coup_possible(L,0)==True
coup_possible(L,2)==True