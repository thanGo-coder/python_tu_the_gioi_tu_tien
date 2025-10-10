n=int(input(     ))
for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==4 or j==0 or j==4:
            print("*" ,end=' ')
        else:
            print(" ",end=' ')
    print( )


