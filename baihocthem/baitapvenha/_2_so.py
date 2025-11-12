# ### **Bài 2: Kiểm tra số âm, dương hay bằng 0**

# - **Mô tả**:
    
#     Nhập một số nguyên, kiểm tra xem số đó là **số dương**, **âm**, hay **bằng 0**.
    
# - **Input**:
    
#     `n = -5`
    
# - **Output**:
    
#     `"Số âm"`
so=int(input("nhapso     "))
if so>=0:
    print("soduong")
elif so==0:
    print("so0")
else:
    print("soam")