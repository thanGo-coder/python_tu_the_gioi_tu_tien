n=int(input(  ))
s=0
i=0
# for i in range (n):
#     a=n%10
#     s=s+a
#     n=n//10
# print(s)
while n!=0:
    a=n%10
    s=s+a
    n=n//10
print(s)
