n=int(input( "nhap" ))
for i in range(0,n):
    for j in range(0,n):
        if i==2 and j==2:
            print("o",end=" ")  
        if (i==0 and j==0) or (i==0 and j==4) or (i==4 and j==0) or (i==4 and j==4):
            print("x",end=' ')
            continue
        if (i==1 and j==3) or j==1 or j==3:
            print("*" ,end=' ')
        else:
            print(" ",end=' ')
    print( )