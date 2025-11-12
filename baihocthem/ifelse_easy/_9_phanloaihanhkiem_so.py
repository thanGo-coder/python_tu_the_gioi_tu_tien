# ### **Bài 9: Phân loại điểm số chi tiết**

# - **Mô tả:** Cho điểm số `diem`. Phân loại học lực chi tiết.
# - **Yêu cầu:**
#     - Nếu `diem` từ 90 trở lên, in ra "Xuất sắc".
#     - Nếu `diem` từ 80 đến 89, in ra "Giỏi".
#     - Nếu `diem` từ 70 đến 79, in ra "Khá".
#     - Nếu `diem` từ 50 đến 69, in ra "Trung bình".
#     - Ngược lại (dưới 50), in ra "Yếu".
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `diem = 78 # Thay đổi giá trị này`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `diem = 95` **Output:** `Xuất sắc`
#     - **Input:** `diem = 82` **Output:** `Giỏi`
#     - **Input:** `diem = 70` **Output:** `Khá`
#     - **Input:** `diem = 65` **Output:** `Trung bình`
#     - **Input:** `diem = 45` **Output:** `Yếu`
diem=int(input("nhapdiemcuaban     "))
if diem>=90:
    print("xuatsac")
elif diem>=80 and diem<=89:
    print("gioi")
elif diem>=70 and diem<=79:
    print("kha")
elif diem>=60 and diem<=69:
    print("trungbinh")
else:
    print("yeu")
