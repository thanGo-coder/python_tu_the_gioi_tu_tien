# ### Bài 29: Tính thời gian di chuyển

# - **Mô tả:** Viết chương trình nhận vào khoảng cách `khoang_cach_km` (km) và vận tốc trung bình `van_toc_km_h` (km/giờ). Tính và in ra **thời gian di chuyển** tính bằng **giờ, phút và giây**.
# - **Input:**
#     - `khoang_cach_km` (số thực)
#     - `van_toc_km_h` (số thực, giả sử > 0)
# - **Output:**
#     - Dòng 1: Số giờ (số nguyên).
#     - Dòng 2: Số phút (số nguyên).
#     - Dòng 3: Số giây (số nguyên).
# - **Ví dụ:**
    
#     ```python
#     # Input:
#     # khoang_cach_km = 100.0
#     # van_toc_km_h = 40.0
#     # Output:
#     # 2
#     # 30
#     # 0
#     ```
    
# - **Giải thích ví dụ:**
#     - Tổng thời gian (giờ): 100.0/40.0=2.5 giờ.
#     - Giờ nguyên: 2 giờ.
#     - Phần thập phân của giờ: 0.5 giờ.
#     - Số phút: 0.5×60=30 phút.
#     - Số giây (trong trường hợp này là 0).

print(100.0/40.0)
print(0.5*60)
# 2gio30phut
