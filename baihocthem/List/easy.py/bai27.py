# n=[1,2,3,4]
# e=[]
# a=n
# for i in range (len(n)):
#     if n[i] not in e:
#         e.append(n[i])
#         e.append(n[i])
# print(e)
n=[1,2,3,4]
for i in range (len(n)):
    n.insert(i,n[i])
    i=i+1
print(n)