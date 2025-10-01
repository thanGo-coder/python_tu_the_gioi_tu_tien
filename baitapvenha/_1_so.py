# ### **Bài 1: Kiểm tra số chẵn hay lẻ**

# - **Mô tả**:
    
#     Nhập một số nguyên từ bàn phím. Kiểm tra xem số đó là **chẵn** hay **lẻ**.
    
# - **Input**:
    
#     Một số nguyên `n` (ví dụ: `7`)
    
# - **Output**:
    
#     `"Số lẻ"` hoặc `"Số chẵn"`
so = int(input("Nhập số: "))
if so == 0:
    print("Số 0 là số chẵn và không âm không dương.")
elif so > 0:
    if so % 2 == 0:
        print(f"Số {so} là số chẵn và là số dương.")
    else:
        print(f"Số {so} là số lẻ và là số dương.")
else:
    if so % 2 == 0:
        print(f"Số {so} là số chẵn và là số âm.")
    else:
        print(f"Số {so} là số lẻ và là số âm.")