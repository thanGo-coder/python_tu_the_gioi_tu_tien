# ### **Bài 1: Kiểm tra số chẵn hay lẻ**

# - **Mô tả**:
    
#     Nhập một số nguyên từ bàn phím. Kiểm tra xem số đó là **chẵn** hay **lẻ**.
    
# - **Input**:
    
#     Một số nguyên `n` (ví dụ: `7`)
    
# - **Output**:
    
#     `"Số lẻ"` hoặc `"Số chẵn"`
so=int(input("nhapso     "))
if so%2==0:
    print("sochan")
else:
    print("sole")