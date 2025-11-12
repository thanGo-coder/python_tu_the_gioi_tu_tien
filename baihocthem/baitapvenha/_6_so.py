# ### **Bài 6: Kiểm tra một ký tự là nguyên âm hay phụ âm**

# - **Mô tả**:
    
#     Nhập vào một chữ cái (`a` đến `z`), kiểm tra xem đó là **nguyên âm** (`a, e, i, o, u`) hay **phụ âm**.
    
# - **Input**:
    
#     `c = 'e'`
    
# - **Output**:
    
#     `"Nguyên âm"`
chu=input("nhapchucai    ")
if chu in "a,e,i,o,u":
    print("nguyenam")
else:
    print("phuam")
