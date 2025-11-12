n=int(input( ))
min=99999999999999999999999999
i=0
while i<n :
    n%i==0
    if i<min:
        min=i
    i=i+1
print(i)