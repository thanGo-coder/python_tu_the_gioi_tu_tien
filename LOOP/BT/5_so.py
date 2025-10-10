i=1
dem=0
N=int(input("nhap N  "))
for i in range (1,N+1):
    if N%i==0:
        dem=dem+1
print(dem)


