# Bài 1: Xác định Loại Năm (Năm Nhuận Nâng Cao)
# Mô tả bài toán: Cho một năm nam. Xác định xem đó có phải là năm nhuận hay không.
# Input: Một số nguyên nam.
# Output: In ra "Đây là năm nhuận." hoặc "Đây KHÔNG phải là năm nhuận."
# Ràng buộc: 0 <= nam <= 3000
# Điều kiện năm nhuận:
# Năm đó chia hết cho 400.
# HOẶC năm đó chia hết cho 4 nhưng KHÔNG chia hết cho 100.
# Ví dụ kiểm thử:
# Input: nam = 2000
# Output: Đây là năm nhuận.

# Input: nam = 2024
# Output: Đây là năm nhuận.

# Input: nam = 1900
# Output: Đây KHÔNG phải là năm nhuận.

# Input: nam = 2023
# Output: Đây KHÔNG phải là năm nhuận.
nam=int(input("nhapsonam   "))
if (nam%4==0 and nam%100!=0) or nam%400==0:
    print("namnhuan")
else:
    print("namkonhuan")