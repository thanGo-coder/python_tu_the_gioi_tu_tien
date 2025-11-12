s=0
i=1
n=int(input("nhap n   "))
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print("yes")
else:
    print("no")