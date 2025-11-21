n=int(input( ))
l=[]
for i in range (n):
    t=int(input())
    l.append(t)
    l.sort()
print(l)
for i in range (n):
    if i==n-1:     
        print(f'{l[i]}',end=' ')
    else:
        print(f'{l[i]} +',end=' ')
