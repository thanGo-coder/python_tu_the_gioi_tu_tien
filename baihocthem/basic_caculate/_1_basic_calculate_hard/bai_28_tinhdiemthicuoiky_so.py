# ### Bài 28: Tính điểm thi cuối kỳ (có trọng số)

# - **Mô tả:** Viết chương trình nhận vào điểm bài tập `diem_bai_tap`, điểm giữa kỳ `diem_giua_ky` và điểm cuối kỳ `diem_cuoi_ky`. Tính và in ra **điểm tổng kết** của học sinh, biết rằng mỗi loại điểm có trọng số khác nhau.
# - **Trọng số:**
#     - Bài tập: 20%
#     - Giữa kỳ: 30%
#     - Cuối kỳ: 50%
# - **Input:**
#     - Ba số thực `diem_bai_tap`, `diem_giua_ky`, `diem_cuoi_ky`.
# - **Output:**
#     - Một số thực duy nhất là điểm tổng kết.
# - **Ví dụ:**
    
#     ```python
#     # Input:
#     # diem_bai_tap = 9.0
#     # diem_giua_ky = 7.0
#     # diem_cuoi_ky = 8.0
#     # Output:
#     # 7.9
#     ```
    
# - **Giải thích ví dụ:** (9.0×0.20)+(7.0×0.30)+(8.0×0.50)=1.8+2.1+4.0=7.9.



print((9.0*0.20)+(7.0*0.30)+(8.0*0.50))