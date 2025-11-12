# ### **Bài 10: Kiểm tra trạng thái nước**

# - **Mô tả:** Cho nhiệt độ của nước `nhiet_do_nuoc` (số nguyên). Biết rằng nước đóng băng ở 0 độ C và sôi ở 100 độ C.
# - **Yêu cầu:**
#     - Nếu `nhiet_do_nuoc` nhỏ hơn hoặc bằng 0, in ra "Nước ở thể rắn (đóng băng)".
#     - Nếu `nhiet_do_nuoc` lớn hơn 0 VÀ nhỏ hơn 100, in ra "Nước ở thể lỏng".
#     - Nếu `nhiet_do_nuoc` lớn hơn hoặc bằng 100, in ra "Nước ở thể khí (hơi nước)".
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `nhiet_do_nuoc = 50 # Thay đổi giá trị này`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `nhiet_do_nuoc = -5` **Output:** `Nước ở thể rắn (đóng băng)`
#     - **Input:** `nhiet_do_nuoc = 0` **Output:** `Nước ở thể rắn (đóng băng)`
#     - **Input:** `nhiet_do_nuoc = 25` **Output:** `Nước ở thể lỏng`
#     - **Input:** `nhiet_do_nuoc = 99` **Output:** `Nước ở thể lỏng`
#     - **Input:** `nhiet_do_nuoc = 100` **Output:** `Nước ở thể khí (hơi nước)`
#     - **Input:** `nhiet_do_nuoc = 120` **Output:** `Nước ở thể khí (hơi nước)`
nhietdo=int(input("nhapnhietdonuoc         "))
if nhietdo<=0:
    print("nuocotheran")
# elif nhietdo>0 and nhietdo<100:
elif 0<nhietdo<100:
    print("nuocothelong")
else:
    print("nuocothekhi")




