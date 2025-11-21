# ### **Bài 1: Tổng của hai số**

# - **Mô tả:** Viết một hàm nhận vào hai số nguyên và trả về tổng của chúng.
# - **Signature:**
    
#     **Python**
    
#     `def tinh_tong(a: int, b: int) -> int:
#         pass`

def tinh_tong(a,b)->int:
    return a+b

a=int(input("nhap a"))
b=int(input("nhap b"))
ket_qua = tinh_tong(a,b)
print(ket_qua)