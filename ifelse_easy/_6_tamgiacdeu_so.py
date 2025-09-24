# ### **Bài 6: Xác định loại hình học (Tam giác cân/đều)**

# - **Mô tả:** Cho ba cạnh của một tam giác `canh1`, `canh2`, `canh3`.
# - **Yêu cầu:**
#     - Nếu ba cạnh bằng nhau, in ra "Tam giác đều".
#     - Nếu có ít nhất hai cạnh bằng nhau (nhưng không phải cả ba), in ra "Tam giác cân".
#     - Ngược lại, in ra "Tam giác thường".
#     - (Bỏ qua điều kiện kiểm tra tam giác hợp lệ để tập trung vào if-else).
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `canh1 = 5 # Thay đổi giá trị này
#     canh2 = 5 # Thay đổi giá trị này
#     canh3 = 3 # Thay đổi giá trị này`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `canh1 = 3, canh2 = 3, canh3 = 3` **Output:** `Tam giác đều`
#     - **Input:** `canh1 = 4, canh2 = 4, canh3 = 5` **Output:** `Tam giác cân`
#     - **Input:** `canh1 = 6, canh2 = 8, canh3 = 10` **Output:** `Tam giác thường`
#     - **Input:** `canh1 = 5, canh2 = 3, canh3 = 5` **Output:** `Tam giác cân`
canh1=int(input("nhapsocuacanh        "))
canh2=int(input("nhapsocuacanh        "))
canh3=int(input("nhapsocuacanh        "))
if canh1==canh2 or canh2==canh3 or canh1==canh3:
    print("tamgiacdeu")
else:
    print("tamgiacthuong")
