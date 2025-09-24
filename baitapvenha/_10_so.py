# ### **Bài 10: Xếp loại tuổi**

# - **Mô tả**:
    
#     Nhập số tuổi, phân loại:
    
#     - Dưới 6: "Mẫu giáo"
#     - 6–10: "Tiểu học"
#     - 11–14: "THCS"
#     - 15–17: "THPT"
#     - Trên 17: "Đã tốt nghiệp phổ thông"
tuoi=int(input("nhaptuoicuabn      "))
if tuoi<6:
    print("mamnon")
elif tuoi>=6 and tuoi<=10:
    print("tieuhoc")
elif tuoi >=11 and tuoi<=14:
    print("thcs")
elif tuoi >=15 and tuoi<=17:
    print("thpt")
else:
    print("dtnpt")