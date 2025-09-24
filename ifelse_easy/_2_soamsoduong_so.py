# ### **Bài 2: Xác định loại số phức tạp**

# - **Mô tả:** Cho một số nguyên `num`. Xác định tính chất của số đó.
# - **Yêu cầu:**
#     - Nếu `num` là **số dương VÀ là số chẵn**, in ra "Số dương chẵn".
#     - Nếu `num` là **số dương VÀ là số lẻ**, in ra "Số dương lẻ".
#     - Nếu `num` là **số âm**, in ra "Số âm".
#     - Nếu `num` là **0**, in ra "Số 0".
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `num = -5 # Thay đổi giá trị này`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `num = 4` **Output:** `Số dương chẵn`
#     - **Input:** `num = 7` **Output:** `Số dương lẻ`
#     - **Input:** `num = -3` **Output:** `Số âm`
#     - **Input:** `num = 0` **Output:** `Số 0`
so=int(input("nhapso     "))
if so<=0:
    if so==0:
        print("so_0")
    print("so_am")
else:
    if so%2==0:
        print("sochan")
    else:
        print("sole")
    print("so_duong")