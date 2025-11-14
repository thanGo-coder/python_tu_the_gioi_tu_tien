# ### **Bài 17: Đổi điểm số sang chữ**

# - **Mô tả**:
    
#     Nhập điểm từ 0–10, in ra chữ cái tương ứng:
    
#     - 9–10: A
#     - 8–<9: B
#     - 7–<8: C
#     - 6–<7: D
#     - <6: F
# - **Input**:
    
#     `diem = 8.5`
    
# - **Output**:
    
#     `"Hạng B"`
diem=float(input("nhapdiemcuaban      "))
if diem >=9:
    print("A")
elif diem >=8:
    print("B")
elif diem>=7:
    print("C")
elif diem>=6:
    print("D")
else:
    print("F")