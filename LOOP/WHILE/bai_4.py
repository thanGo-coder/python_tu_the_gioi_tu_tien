n=int(input( ))
i=1
hangxom=0
t=n
while t!=0:
    a=t%10
    hangxom=hangxom*10+a
    t=t//10
if hangxom==n:
    print("yes")
else:
    print("no")