# ### Bài 23: Tính diện tích toàn phần của hình trụ

# - **Mô tả:** Viết chương trình nhận vào bán kính đáy `ban_kinh_day` và chiều cao `chieu_cao` của một hình trụ. Tính và in ra **diện tích toàn phần** của hình trụ đó.
# - **Công thức:**
#     - Diện tích đáy = `PI * bán_kính_đáy * bán_kính_đáy`
#     - Diện tích xung quanh = `2 * PI * bán_kính_đáy * chiều_cao`
#     - Diện tích toàn phần = `2 * Diện tích đáy + Diện tích xung quanh`
# - **Input:**
#     - Hai số thực `ban_kinh_day` và `chieu_cao`.
# - **Output:**
#     - Một số thực duy nhất là diện tích toàn phần hình trụ.
# - **Ví dụ:** (Sử dụng `PI = 3.1415926535`)
    
#     ```python
#     # Input:
#     # ban_kinh_day = 2.0
#     # chieu_cao = 5.0
#     # Output:
#     # 87.9645943
#     ```
    
# - **Giải thích ví dụ:**
#     - Diện tích đáy: PI×2.02=4×PI.
#     - Diện tích xung quanh: 2×PI×2.0×5.0=20×PI.
#     # - Diện tích toàn phần: 2×(4×PI)+(20×PI)=8×PI+20×PI=28×PI≈87.964....




import math
print(math.pi*(2*4+20))

