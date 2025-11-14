# ### **Bài 7: Tính điểm trung bình và xếp loại**

# - **Mô tả**:
    
#     Nhập điểm 3 môn, tính điểm trung bình và xếp loại theo quy tắc:
    
#     - TB >= 8: Giỏi
#     - TB >= 6.5: Khá
#     - TB >= 5: Trung bình
#     # - Dưới 5: Yếu
diem=int(input("nhapdiemcuaban      "))
if diem>=8:
    print("gioi")
elif diem>=6.5:
    print("kha")
elif diem>=5:
    print("trungbinh")
else:
    print("yeu")