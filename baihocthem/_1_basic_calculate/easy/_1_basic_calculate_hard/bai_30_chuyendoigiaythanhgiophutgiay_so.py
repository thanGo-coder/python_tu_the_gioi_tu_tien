# ### Bài 30: Chuyển đổi giây thành giờ, phút, giây

# - **Mô tả:** Viết chương trình nhận vào tổng số giây `tong_so_giay`. Chuyển đổi và in ra số giờ, số phút và số giây còn lại.
# - **Input:**
#     - Một số nguyên `tong_so_giay` (giả sử không âm).
# - **Output:**
#     - Dòng 1: Số giờ (số nguyên).
#     - Dòng 2: Số phút (số nguyên).
#     - Dòng 3: Số giây còn lại (số nguyên).
# - **Ví dụ:**
    
#     ```python
#     # Input:
#     # tong_so_giay = 3665
#     # Output:
#     # 1
#     # 1
#     # 5
#     ```
    
# - **Giải thích ví dụ:**
#     - Số giờ: 3665÷3600=1 (dư 65)
#     - Số phút: 65÷60=1 (dư 5)
#     - Số giây còn lại: 5

print(3665//3600)
print(65//60)
print(5)
