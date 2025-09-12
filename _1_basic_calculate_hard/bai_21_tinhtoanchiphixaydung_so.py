# ### Bài 21: Tính toán chi phí xây dựng hàng rào

# - **Mô tả:** Viết chương trình nhận vào chiều dài `dai` và chiều rộng `rong` của một khu vườn hình chữ nhật. Tính và in ra tổng chi phí để xây dựng hàng rào xung quanh khu vườn, biết rằng chi phí vật liệu là `gia_vat_lieu_tren_met` (VNĐ/mét) và chi phí nhân công là `gia_nhan_cong_tren_met` (VNĐ/mét).
# - **Input:**
#     - `dai` (số thực), `rong` (số thực)
#     - `gia_vat_lieu_tren_met` (số nguyên), `gia_nhan_cong_tren_met` (số nguyên)
# - **Output:**
#     - Một số nguyên duy nhất là tổng chi phí xây dựng hàng rào.
# - **Ví dụ:**
    
#     ```python
#     # Input:
#     # dai = 10.0, rong = 5.0
#     # gia_vat_lieu_tren_met = 50000
#     # gia_nhan_cong_tren_met = 20000
#     # Output:
#     # 2100000
#     ```
    
# - **Giải thích ví dụ:**
#     - Chu vi khu vườn: 2×(10.0+5.0)=30.0 mét.
#     - Tổng chi phí trên mỗi mét: 50000+20000=70000 VNĐ/mét.
#     - Tổng chi phí: 30.0×70000=2100000 VNĐ.

print(2*(10.+5.0))
print(50000+20000)
print(30.0*70000)