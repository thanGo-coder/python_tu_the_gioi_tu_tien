# ### **Bài 9: Kiểm tra mật khẩu**

# - **Mô tả**:
    
#     Nhập mật khẩu từ bàn phím. Nếu đúng là `"12345"` thì báo `"Đăng nhập thành công"`, sai thì `"Sai mật khẩu"`.
    
# - **Input**:
    
#     `"12345"`
    
# - **Output**:
    
#     `"Đăng nhập thành công"`
mk=(input("nhapmk     "))
if mk=='123456':
    print("mkdadung")
else:
    print("mkdasai")