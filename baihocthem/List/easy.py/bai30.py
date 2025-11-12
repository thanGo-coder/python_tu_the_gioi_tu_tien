n=[10,50,90,5,30]
s=0
x=int(input( ))
n.sort()
for i in range (len(n)):
    if n[i]>x:
        s=s+1
print(s)