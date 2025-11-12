n=[1,2,3,4,5]
e=0
s=0
for i in range (len(n)):
    if n[i]%2==0:
        s=s+n[i]
    else:
        e=e+n[i]
print('sochan',s)
print('sole',e)