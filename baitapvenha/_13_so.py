# ### **Bài 13: Kiểm tra tam giác hợp lệ**

# - **Mô tả**:
    
#     Nhập ba cạnh `a, b, c`. Kiểm tra xem có tạo thành tam giác không. Điều kiện: tổng 2 cạnh phải lớn hơn cạnh còn lại.
    
# - **Input**:
    
    
# - **Output**:
    
#     `"Là tam giác"`
A=int(input("nhapcanhA  "))
B=int(input("nhapcanhB  "))
C=int(input("nhapcanhC  "))
if A+B>C or A+C>B or B+C>A or B+A>C or C+B>A or C+A>B:
    print("la tam giac")
else:
    print("ko phai la tam giac")