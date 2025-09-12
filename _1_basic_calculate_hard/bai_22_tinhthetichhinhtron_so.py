# ### Bài 22: Tính thể tích hình nón

# - **Mô tả:** Viết chương trình nhận vào bán kính đáy `ban_kinh_day` và chiều cao `chieu_cao` của một hình nón. Tính và in ra **thể tích** của hình nón đó.
# - **Công thức:** Thể tích = `(1/3) * PI * bán_kính_đáy * bán_kính_đáy * chiều_cao`
# - **Input:**
#     - Hai số thực `ban_kinh_day` và `chieu_cao`.
# - **Output:**
#     - Một số thực duy nhất là thể tích hình nón.
# - **Ví dụ:** (Sử dụng `PI = 3.1415926535`)
    
#     ```python
#     # Input:
#     # ban_kinh_day = 3.0
#     # chieu_cao = 4.0
#     # Output:
#     # 37.699111842
#     ```
    
# - **Giải thích ví dụ:** 31×PI×3.02×4.0=31×PI×9.0×4.0=12.0×PI≈37.699....
import math



print(math.pi*(3.0*4.0))



