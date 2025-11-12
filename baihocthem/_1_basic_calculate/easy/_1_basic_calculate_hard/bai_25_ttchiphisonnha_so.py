# ### Bài 25: Tính toán chi phí sơn nhà

# - **Mô tả:** Viết chương trình nhận vào chiều dài `chieu_dai_phong`, chiều rộng `chieu_rong_phong` và chiều cao `chieu_cao_phong` của một căn phòng. Tính và in ra tổng chi phí để sơn bốn bức tường của căn phòng đó, biết giá sơn là `gia_son_tren_met_vuong` (VNĐ/mét vuông). Bỏ qua diện tích cửa và các vật cản khác.
# - **Input:**
#     - `chieu_dai_phong` (số thực), `chieu_rong_phong` (số thực), `chieu_cao_phong` (số thực)
#     - `gia_son_tren_met_vuong` (số nguyên)
# - **Output:**
#     - Một số nguyên duy nhất là tổng chi phí sơn.
# - **Ví dụ:**
    
#     ```python
#     # Input:
#     # chieu_dai_phong = 5.0, chieu_rong_phong = 4.0, chieu_cao_phong = 3.0
#     # gia_son_tren_met_vuong = 25000
#     # Output:
#     # 1350000
#     ```
    
# - **Giải thích ví dụ:**
#     - Chu vi đáy phòng: 2×(5.0+4.0)=18.0 mét.
#     - Diện tích bốn bức tường (diện tích xung quanh): 18.0×3.0=54.0 mét vuông.
#     - Tổng chi phí sơn: 54.0×25000=1350000 VNĐ.
chuvidayphong=2*(5.0+4.0)
DTbonbuctuong=18.0*3.0
print(DTbonbuctuong*25000)
