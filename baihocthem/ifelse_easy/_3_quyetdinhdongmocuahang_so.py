# ### **Bài 3: Quyết định mở/đóng cửa hàng theo giờ và ngày**

# - **Mô tả:** Cho giờ hiện tại `gio_hien_tai` (số nguyên từ 0 đến 23) và `la_cuoi_tuan` (boolean, `True` nếu là cuối tuần, `False` nếu không). Cửa hàng mở cửa từ 9h đến 18h các ngày trong tuần, và đóng cửa vào cuối tuần.
# - **Yêu cầu:** In ra "Cửa hàng đang mở" hoặc "Cửa hàng đang đóng".
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `gio_hien_tai = 10 # Thay đổi giá trị này
#     la_cuoi_tuan = False # Thay đổi giá trị này`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `gio_hien_tai = 12, la_cuoi_tuan = False` **Output:** `Cửa hàng đang mở`
#     - **Input:** `gio_hien_tai = 8, la_cuoi_tuan = False` **Output:** `Cửa hàng đang đóng`
#     - **Input:** `gio_hien_tai = 19, la_cuoi_tuan = False` **Output:** `Cửa hàng đang đóng`
#     - **Input:** `gio_hien_tai = 12, la_cuoi_tuan = True` **Output:** `Cửa hàng đang đóng`
gio=int(input("giolamaygio        "))
lacuoituan=True
if gio>=9 and gio<18:
    if lacuoituan==False:

        print("open")
    else:
        print("close")
else:
    print("close")


