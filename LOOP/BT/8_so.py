a=0
b=1
n=int(input("nhap n    "))
for i in range(3,n+1):
        c=a+b 
        a=b 
        b=c
print(b)