soA=int(input("nhapsoA       "))
soB=int(input("nhapsoB       "))
soC=int(input("nhapsoC       "))
# if soA>soB>soC:
#     print("soAlonnhat")
# elif soA>soC>soB:
#     print("soAlonnhat")
# elif soB>soA>soC:
#     print("soBlonnhat")
# elif soB>soC>soA:
#     print("soBlonnhat")
# elif soC>soB>soC:
#     print("soClonnhat")
# else:
#     print("0")
max=soA
if soA>soB:
    if soA>soC:
        max=soA
    else:
        max=soC
elif soB>soC:
    max=soB
else:
    max=soC


print(max)

