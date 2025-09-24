# ### **Bài 14: Kiểm tra tam giác vuông**

# - **Mô tả**:
    
#     Sau khi đã kiểm tra là tam giác, tiếp tục kiểm tra tam giác có vuông không (theo định lý Pythagoras).
    
# - **Input**:
    
#     `3, 4, 5`
    
# - **Output**:
    
#     `"Tam giác vuông"`
A=int(input("nhapcanhA   "))
B=int(input("nhapcanhB   "))
C=int(input("nhapcanhC   "))
if C**2==A**2+B**2 or B**2==C**2+A**2 or A**2==C**2+B**2:
    print("là tam giác vuông")
else:
    print("ko phải là tam giác vuông")








