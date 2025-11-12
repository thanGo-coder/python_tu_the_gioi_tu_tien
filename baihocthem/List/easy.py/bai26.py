on=[10,20,30,40,599999999999999999999999999]
dex=[1,3]
input=[]
for i in range (len(on)):
    if i not in dex:
        input.append(on[i])
print(input)