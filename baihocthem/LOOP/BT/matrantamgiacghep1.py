n=int(input( ))
for i in range(0,n):
    for j in range(0,i+1):
        print("*" ,end=' ')
    print( )
for i in range (0,n):
    for j in range (0,n):
        if j>i:
            print("*",end=' ')
    print( )
for i in range (n):
    for j in range (n):
        if i+j>=n-1:
            print("*",end=' ')
        else :
            print(" ",end=' ')
    print( )
