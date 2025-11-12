n=int(input( ))
i=1
hangxom=0

while n!=0:
    a=n%10
    hangxom=hangxom*10+a
    n=n//10
print(hangxom)


