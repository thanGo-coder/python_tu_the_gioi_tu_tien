# ### **Bài 1: Kiểm tra tính hợp lệ của tuổi và điểm**

# - **Mô tả:** Cho tuổi `tuoi` và điểm số `diem`. Kiểm tra xem một người có đủ điều kiện để tham gia một cuộc thi hay không.
# - **Yêu cầu:** In ra "Đủ điều kiện tham gia" nếu **tuổi từ 18 trở lên AND điểm số từ 70 trở lên**. Ngược lại, in ra "Không đủ điều kiện tham gia".
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `tuoi = 20 # Thay đổi giá trị này
#     diem = 85 # Thay đổi giá trị này`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `tuoi = 25, diem = 90` **Output:** `Đủ điều kiện tham gia`
#     - **Input:** `tuoi = 17, diem = 80` **Output:** `Không đủ điều kiện tham gia`
#     - **Input:** `tuoi = 18, diem = 65` **Output:** `Không đủ điều kiện tham gia`
#     - **Input:** `tuoi = 18, diem = 70` **Output:** `Đủ điều kiện tham gia`
diem=int(input("nhap_diem_cua_ban    "))
tuoi=int(input("nhap_tuoi_cua_ban    "))
if tuoi >=18 and diem >=70:
    print("ban_da_du_dieu_kien")
else:
    print("ko")
