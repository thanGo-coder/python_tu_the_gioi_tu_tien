# ### **Bài 5: Kiểm tra số có 2 chữ số**

# - **Mô tả:** Cho một số nguyên `so`. Kiểm tra xem số đó có phải là số có hai chữ số hay không (từ 10 đến 99 hoặc từ -99 đến -10).
# - **Yêu cầu:** In ra "Đây là số có hai chữ số" nếu đúng. Ngược lại, in ra "Đây KHÔNG phải là số có hai chữ số".
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `so = 42 # Thay đổi giá trị này`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `so = 25` **Output:** `Đây là số có hai chữ số`
#     - **Input:** `so = 7` **Output:** `Đây KHÔNG phải là số có hai chữ số`
#     - **Input:** `so = 100` **Output:** `Đây KHÔNG phải là số có hai chữ số`
#     - **Input:** `so = -55` **Output:** `Đây là số có hai chữ số`
#     - **Input:** `so = -5` **Output:** `Đây KHÔNG phải là số có hai`
so=int(input("nhapsoco2chuso       "))
if so>=10 and so<=99  or so>=-99 and so<=-10:
    print("daylasoco2chuso")
else:
    print("daykophailasoco2chuso")