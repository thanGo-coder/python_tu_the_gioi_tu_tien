n=int(input( ))
a=int(input( "nhap" ))  
dem=1
for i in range(1,n+1):
    print(i,end=' ')
    if dem==3:
        dem=0
        print( )
    dem+=1
for i in range(0,a):
    for j in range(0,a):
        if i==2 and j==2:
            print("o",end=" ")
            continue
        if i==0 or i==4 or j==0 or j==4:
            print("*" ,end=' ')
        else:
            print(" ",end=' ')
    print( )
