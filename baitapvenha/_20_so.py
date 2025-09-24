# ### **Bài 20: Tính ngày trong tháng**

# - **Mô tả**:
        #  Nhap nam kiem tra no phai nam nhuan khong 
#     Nhập vào số tháng (1–12), in ra số ngày:
    
#     - Tháng 1,3,5,7,8,10,12: 31 ngày
#     - Tháng 4,6,9,11: 30 ngày
#     - Tháng 2: 28 hoặc 29 (giả sử 28)
# - **Input**:
    
#     `thang = 2`
    
# - **Output**:
    
#     `"Tháng 2 có 28 ngày"`
thang=int(input("nhapsothang    "))
nam=int(input("nhapsonam    "))
if thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12:
    print("co 31 day")
elif thang==4 or thang==6 or thang==9 or thang==11:
    print("co 30 day")
elif thang==2:
   
    if (nam%4==0 and nam%100!=0) or nam%400==0:
        print("co 29 day")
    else:
        print("co 28 day")
else:
    print("NO have")
# if (nam%4==0 and nam%100!=0) or nam%400==0:
#     print("nam nhuan ")
# else:
#     print("namkonhuan")





