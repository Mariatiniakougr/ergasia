import random
T = [[0 for i in range(10)] for i in range(20)]
b=True
L=0
while(b==True):
    y= random.randrange(9)
    xx=True
    for x in range(20):
        if(T[x][y]==0 and T[x][y+1]==0 and xx==True):
            if(x+2<=19):
                T[x][y]=L
                T[x][y+1]=L
                T[x+1][y]=L
                T[x+2][y]=L
                L+=1
                xx=False
            else:
                b=False
print L," L's have been inserted successfully"
